import getgeo
import pandas as pd
from wetterdienst.provider.dwd.forecast import (
    DwdForecastDate,
    DwdMosmixRequest,
    DwdMosmixType,
)
import wetterdienst as wetterdienst
import os

#TODO start time

def mosmix_forecast(address,weather_parameters,humanize=True):
    """
    Gives back a df with the weather forecast for the nearest weather station to a chosen address.
        Parameters:
            address (string): chosen address
            weather_parameters (list of string): list of short names of weather parameters
            humanize (bool): short names of weather parameters are renamed with description
        Returns:
            df_weather_forecast: df with weather forecast for chosen parameters
    """

    # latitude and longitude value from mapquest in decimal degree
    lat=getgeo.get_long_lat(address)["lat"]
    lng=getgeo.get_long_lat(address)["lng"]

    #conversion of coordinates in degree minutes
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
    lat_min=decdeg2dms(lat)
    lng_min=decdeg2dms(lng)

    #get nearest weather station
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path_mosmix=os.path.join(__location__,"DWD data\mosmix stations cleaned.csv")
    mosmix_stations=pd.read_csv(path_mosmix,delimiter=";")
    nump_lat=mosmix_stations["nb."].values
    nump_lng=mosmix_stations["el."].values
    coordinates=wetterdienst.util.geo.Coordinates(lat_min,lng_min)
    nearest_station=wetterdienst.util.geo.derive_nearest_neighbours(nump_lat,nump_lng,coordinates,1)
    station_name=mosmix_stations.loc[nearest_station[1],"name"]
    station_id=mosmix_stations.loc[nearest_station[1],"id"]

    #request weather forecast from Mosmix small station (MOSMIX_S (24x daily, 40 parameters, up to +240h)) 
    request = DwdMosmixRequest(
        parameter=weather_parameters,
        start_issue=DwdForecastDate.LATEST, 
        mosmix_type=DwdMosmixType.SMALL,
        tidy=False,
        humanize=humanize,
    )
    stations = request.filter_by_station_id(
        station_id,
    )
    response = next(stations.values.query())
    #create df
    df_weather_forecast=response.df
    df_weather_forecast.insert(loc = 0,
          column = 'station_name',
          value = station_name)
    return(df_weather_forecast)

