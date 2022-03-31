import pandas as pd
import plotly
import plotly.graph_objects
import plotly.express

def get_plotly_string(df:pd.DataFrame) -> str:
    data = extract_data(df)
    div = plotly.offline.plot(data, include_plotlyjs=False, output_type='div')
    return div

def open_plotly_html(df:pd.DataFrame):
    data = extract_data(df)
    plotly.offline.plot(data, filename="prediction.html")

def extract_data(df:pd.DataFrame):
    trace = plotly.graph_objects.Scatter(x=df['date'], y=df['P_gen [kW]'])
    data = [trace]
    return data