import pandas as pd

#pd.read_csv('data\weather\DWD\mosmix_stations.txt', names=['Date','AgentName','Group','Direction'], skiprows=1, sep='\t')

#df=pd.read_csv('data\weather\DWD\mosmix_stations.txt', sep='\t',encoding='utf-8-sig')
#print(df)

import magic


blob = open('data\weather\DWD\mosmix_stations.txt', 'rb').read()
m = magic.Magic(mime_encoding=True)
encoding = m.from_buffer(blob)

df=pd.read_csv('data\weather\DWD\mosmix_stations.txt', sep='\t',encoding=encoding)
print(df)
