import pandas as pd
import os
import matplotlib.pyplot as plt

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