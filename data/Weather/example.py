from weather_forecast import mosmix_forecast
import matplotlib.pyplot as plt 

address="Auf der Reihe 2, 45884 Gelsenkirchen,Germany"

df_weather=mosmix_forecast(address,["Rad1h"],humanize=False)

df_weather.plot(x="date",y="value")

plt.show()

print("test")