import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('solar-score\data\weather\MetElementDefinition.xml')
root=tree.getroot()
weather_descrption=[]

for descr in root.iter('Description'):
    weather_descrption.append(descr.text)
print(weather_descrption)
df = pd.Series(weather_descrption) 
df.to_csv("Weather Parameters.csv",sep=";")