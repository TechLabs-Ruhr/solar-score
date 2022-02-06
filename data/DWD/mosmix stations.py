import pandas as pd
import os
import io

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
path_text=os.path.join(__location__,"mosmix_stations.txt")
encoding='iso-8859-1'
#TODO Split if more than two spaces occur
with io.open(path_text, mode="r", encoding=encoding) as f:
    for line in f:
        print(line.split())

