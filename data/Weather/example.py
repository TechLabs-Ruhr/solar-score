import os
import sys
from pathlib import Path
path = Path(os.getcwd()).parent.parent
print(path)
sys.path.append(path)
from data.core.fetching import mosmix_forecast
import matplotlib.pyplot as plt 

address="Auf der Reihe 2, 45884 Gelsenkirchen,Germany"

df_weather=mosmix_forecast(address,["Rad1h"],humanize=False)

df_weather.plot(x="date",y="value")

print(df_weather)