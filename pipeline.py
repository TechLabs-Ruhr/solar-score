import pandas as pd
from data.core import fetching, drawing
from prediction.core import inferencing

df = fetching.get_forecast_dataframe()
print(inferencing.dataframe.predict(df).preds)