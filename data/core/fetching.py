from fileinput import filename
import os
import pandas as pd
import numpy as np
import requests
import json
import wetterdienst as wetterdienst
import pickle
from dotenv import load_dotenv
from pathlib import Path
from wetterdienst.provider.dwd.mosmix import DwdForecastDate, DwdMosmixRequest, DwdMosmixType
from wetterdienst import Settings


def get_forecast_dataframe(address:str=None) -> pd.DataFrame:
    """Fetches the newest weather forecast and prepares the data for usage in calculation pipeline."""
    df = mosmix_forecast(address=address)
    df = clean_dataframe(df)
    df = rename_columns(df)
    return df

def get_test_dataframe() -> pd.DataFrame:
    """Creates random data for testing other pipeline components."""
    parameters = list(utility.get_column_dict().values())
    print(parameters)
    df = pd.DataFrame(columns=parameters)
    df['Date'] = np.linspace(1, 240, 240)
    for parameter in parameters:
        df[parameter] = np.random.random((240))
    return df

def clean_dataframe(df:pd.DataFrame) -> pd.DataFrame:
    """Prepares DataFrame for usage in calculation pipeline."""
    if 'parameter' not in df:
        print("Column \"parameter\" not found in DataFrame.")
        return
    if 'date' not in df:
        print("Column \"date\" not found in DataFrame.")
        return
    
    nw = pd.DataFrame()
    unique_parameter = df['parameter'].unique().tolist()
    nw['Date'] = df.loc[df.parameter == unique_parameter[0], "date"]

    for parameter in unique_parameter:
        nw[parameter] = df.loc[df.parameter == parameter, "value"].to_numpy()
    
    return nw

def rename_columns(df:pd.DataFrame) -> pd.DataFrame:
    mapping = utility.get_column_dict()

    df.columns = map(str.lower, df.columns)
    df.rename(columns=mapping, inplace=True)    
    return df

def mosmix_forecast(address:str=None, weather_parameters:list=None, humanize:bool=False) -> pd.DataFrame:
    """
    Gives back a df with the weather forecast for the nearest weather station to a chosen address.
        Parameters:
            address (string): chosen address
            weather_parameters (list of string): list of short names of weather parameters
            humanize (bool): short names of weather parameters are renamed with description
        Returns:
            df_weather_forecast: df with weather forecast for chosen parameters
    """

    if weather_parameters is None:
        weather_parameters = utility.get_column_dict().keys()

    # latitude and longitude value from mapquest in decimal degree
    lnglat = utility.get_long_lat(address)
    lat = lnglat["lat"]
    lng = lnglat["lng"]

    # conversion of coordinates in degree minutes
    def decdeg2dms(dd):
        """
        Converts coordinates in decimal degrees in degree minutes
            Parameters:
                dd (float): coordinates in decimal minutes
            Returns:
                coordiantes in degree minutes
        """
        is_positive = dd >= 0
        dd = abs(dd)
        minutes = dd*3600/60
        degrees,minutes = divmod(minutes,60)
        degrees = degrees if is_positive else -degrees
        if len(str(round(minutes)))==1:
            dms_string=str(round(degrees))+".0"+str(round(minutes))
        else:
            dms_string=str(round(degrees))+"."+str(round(minutes))
        dms=float(dms_string)
        return dms    
    lat_min = decdeg2dms(lat)
    lng_min = decdeg2dms(lng)

    # get nearest weather station
    path_mosmix = Path(__file__).parent / "mosmix stations cleaned.csv"
    mosmix_stations = pd.read_csv(path_mosmix, delimiter=";")
    nump_lat = mosmix_stations["nb."].values
    nump_lng = mosmix_stations["el."].values
    coordinates = wetterdienst.util.geo.Coordinates(lat_min,lng_min)
    nearest_station = wetterdienst.util.geo.derive_nearest_neighbours(nump_lat,nump_lng,coordinates,1)
    station_name = mosmix_stations.loc[nearest_station[1],"name"]
    station_id = mosmix_stations.loc[nearest_station[1],"id"]

    #request weather forecast from Mosmix small station (MOSMIX_S (24x daily, 40 parameters, up to +240h)) 
    Settings.tidy = False
    Settings.humanize = humanize

    request = DwdMosmixRequest(
        parameter=weather_parameters,
        start_issue=DwdForecastDate.LATEST, 
        mosmix_type=DwdMosmixType.SMALL,
    )
    stations = request.filter_by_station_id(
        station_id,
    )
    response = next(stations.values.query())
    # create df
    df_weather_forecast=response.df
    df_weather_forecast.insert(loc = 0,
          column = 'station_name',
          value = station_name)

    return df_weather_forecast

class utility:
    def get_column_dict(filename:str="weather parameter mapping.pkl") -> dict:
        with open(Path(__file__).parent / filename, 'rb') as f:
            mapping:dict = pickle.load(f)
        return mapping

    def get_long_lat(address) -> dict:
        """
        Gives back dict with latitude and longitude value of an adress. Request made via mapquest.

            Parameters:
                address (str): address of which latidude and longitude are requested

            Returns:
                dict with latidude and longitude of address
        """    

        if address is None:
            address = "Auf der Reihe 2, 45884 Gelsenkirchen, Germany"

        # input: address and API key
        load_dotenv()
        parameters = {
            "key": os.getenv("api_key"),
            "location": address
        }

        # respone from mapquest
        response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
        data = response.text
        dataJ = json.loads(data)['results']

        # save latitude and longitude value in dict
        dict_geo={}
        lat = (dataJ[0]['locations'][0]['latLng']['lat'])
        dict_geo["lat"]=lat
        lng = (dataJ[0]['locations'][0]['latLng']['lng'])
        dict_geo["lng"]=lng

        return dict_geo