import pandas as pd
from matplotlib import pyplot as plt
from weather_forecast import mosmix_forecast


df_weather=mosmix_forecast("August-Schmidt-Straße 1, 44227 Dortmund, Germany",["TTT","N","Rad1h"],humanize=False)


fig, axs = plt.subplots(3)
fig.suptitle('Weather Forecast Dortmund')

df_weather["ttt"] = df_weather["ttt"].subtract(273.15)

axs[0].plot(df_weather["date"], df_weather["ttt"], color="#FFC000")
axs[0].set_ylabel("Temp. 2m above surface [°C]")
axs[0].xaxis.set_ticklabels([])
axs[0].set_xticks([])
axs[1].plot(df_weather["date"], df_weather["n"], color="#FFC000")
axs[1].set_ylabel("Total cloud cover [%]")
axs[1].xaxis.set_ticklabels([])
axs[1].set_xticks([])
axs[2].plot(df_weather["date"], df_weather["rad1h"],color="#FFC000")
axs[2].set_ylabel("Global Irradiance [kJ/m²]")
axs[2].tick_params(axis='x', labelrotation = 90)
plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.9, 
                    top=0.94, 
                    wspace=0.2, 
                    hspace=0.1)
plt.show()
