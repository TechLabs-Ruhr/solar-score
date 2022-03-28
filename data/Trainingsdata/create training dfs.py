import pandas as pd
import os
import matplotlib.pyplot as plt

from wetterdienst import Wetterdienst
from wetterdienst.provider.dwd.observation import DwdObservationRequest, DwdObservationDataset, DwdObservationPeriod, DwdObservationResolution
from wetterdienst import Settings
API = Wetterdienst("dwd", "observation")
pd.options.display.max_columns = 8


Settings.tidy = True  # default, tidy data
Settings.humanize = True  # default, humanized parameters
Settings.si_units = True

DwdObservationRequest.discover()

parameters=['radiation_sky_short_wave_diffuse','radiation_sky_long_wave',"radiation_global"]

stations = DwdObservationRequest(
    parameter=parameters,
    resolution="Hourly",
    start_date="2014-01-01",  # if not given timezone defaulted to UTC
    end_date="2014-12-31",
    period=DwdObservationPeriod.HISTORICAL).all()


df_stations = stations.df
df_stations.to_csv("stations.csv",sep=";")

request = DwdObservationRequest(
parameter=parameters,
resolution="hourly",
start_date="2014-01-01",  # if not given timezone defaulted to UTC
end_date="2014-12-31",  # if not given timezone defaulted to UTC
).filter_by_station_id(station_id=(1048))

df_radiation=request.values.all().df
df_radiation["value"]=df_radiation["value"]/1000

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

weather_data=pd.read_csv(os.path.join(__location__,"pre-cleaned CSVs/Weather_Data_cleaned.csv"),delimiter=";")
pv_data=pd.read_csv(os.path.join(__location__,"pre-cleaned CSVs/PV_Data_Customers_Hourly_cleaned.csv"),delimiter=";")

path_output=os.path.join(__location__,"model input CSVs")

weather_data["Time"]=weather_data["Date"]+" "+weather_data["Hour"]
weather_data['Time'] =  pd.to_datetime(weather_data['Time'], format='%d.%m.%Y %I:%M %p')


pv_data['Time'] =  pd.to_datetime(pv_data['datetime'], format='%d.%m.%Y %H:%M')
pv_data.rename(columns = {'Substation':'Site'}, inplace = True)

df_merge = pd.merge(weather_data, pv_data,  how='left', left_on=['Site','Time'], right_on = ['Site','Time'])
df_merge.to_csv("test.csv",sep=";")
sites=["YMCA","Forest Road","Maple Drive East"]
df_input_format=df_merge[["Site","Time","TempOut [K]","DewPt [K]","WindSpeed [m/s]","SolarRad [kJ/m²]","P_gen [kW]"]]
for site in sites:
    df_site=df_input_format[df_input_format["Site"]==site]
    df_site.iloc[:,2:]=df_site.iloc[:,2:].apply(pd.to_numeric)
    list_colums=["TempOut [K]","DewPt [K]","WindSpeed [m/s]","SolarRad [kJ/m²]","P_gen [kW]"]
    fig, ax = plt.subplots(len(list_colums),sharex=True,figsize=(10,12))
    for counter,column in enumerate(list_colums):
        ax[counter].plot(df_site.Time,df_site[column])
        ax[counter].set_title(column) 
    plt.tight_layout()
    filename="input {}".format(site)
    plt.savefig(os.path.join(path_output,"{}.png".format(filename)))
    df_site.to_csv(os.path.join(path_output,"{}.csv".format(filename)),sep=";",index=False)

fig, ax = plt.subplots(3,sharex=True,figsize=(10,12))
for counter,parameter in enumerate(parameters):
    df_radiation_type=df_radiation[df_radiation.parameter==parameter]
    ax[counter].plot(df_radiation_type.date,df_radiation_type.value)
    ax[counter].set_title(parameter)
plt.savefig(os.path.join(path_output,"radiation types DWD.png"))    


