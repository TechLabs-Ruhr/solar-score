import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_xml=os.path.join(__location__,"MetElementDefinition.xml")
xmlp = et.XMLParser(encoding="utf-8")
tree=et.parse(path_xml,parser=xmlp)
root=tree.getroot()
weather_description=[]
shortname=[]
unit_measurement=[]

for descr in root.iter('Description'):
    weather_description.append(descr.text)

for name in root.iter('ShortName'):
    shortname.append(name.text)

for unit in root.iter('UnitOfMeasurement'):
    unit_measurement.append(unit.text)
data=[weather_description,shortname,unit_measurement]
df = pd.DataFrame (data).transpose()
df.columns = ["Weather Parameter", "Short Name", "Unit"]
outpath=os.path.join(__location__,"Weather Parameters.csv")
df.to_csv(outpath,sep=";")