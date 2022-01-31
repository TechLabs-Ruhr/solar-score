import pandas as pd
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_text=os.path.join(__location__,"mosmix_stations.txt")
encoding='iso-8859-1'

df=pd.read_csv(path_text, sep=' ',encoding=encoding, skiprows=2)
df_stations=df["id","name"]
print(df)
