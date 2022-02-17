from weather_forecast import mosmix_forecast

address="Auf der Reihe 2, 45884 Gelsenkirchen,Germany"

df_weather=mosmix_forecast(address,["TTT","N","Rad1h"],humanize=False)

print(df_weather)