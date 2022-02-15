import datetime
from wetterdienst.provider.dwd.mosmix import (
    DwdForecastDate,
    DwdMosmixRequest,
    DwdMosmixType,
)
from wetterdienst import Settings
from pytz import timezone

#start time


def weather_forecast(station_id, weather_parameters, starttime=None, humanize=True):
    """
    Gives back a df with the weather forecast for a chosen weather station for
    a list of weather parameters from a set start time until forecast data
    are not available anymore.

        Parameters:
            weather_station (string): station for which weather data are scraped
            weather_parameters (list of string): list of short names of weather parameters
            start_time (date): time when forecast starts
        Returns:
            df_weather_forecast: df with weather forecast for chosen parameters
    """

    Settings.tidy = False
    Settings.humanize = humanize

   #MOSMIX_S (24x daily, 40 parameters, up to +240h)     
   #tidy: tidy df (parameter gets extra column), humanize: rename short names --> description
    request = DwdMosmixRequest(
        parameter=weather_parameters,
        start_issue=DwdForecastDate.LATEST, 
        mosmix_type=DwdMosmixType.SMALL,
    )
    stations = request.filter_by_station_id(
        station_id,
    )
    response = next(stations.values.query())
    #Metadata
    #df_metaddata=response.stations.df
    df_weather_forecast=response.df
    return(df_weather_forecast)

    