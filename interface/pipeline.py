# import pandas as pd
# from data.core import fetching, drawing
# from prediction.core import inferencing

# def testfetching():
#     """Tests the fetching mechanism for getting weather data."""
#     df = fetching.get_forecast_dataframe()
#     print(df.head())

# def testinferencing():
#     """Tests the inferencing mechanism for predicting power output."""
#     df = fetching.get_test_dataframe()
#     print(inferencing.get_prediction_dataframe(df).head())

# def testdrawing():
#     """Tests the drawing mechanism for creating html-plot-string."""
#     df = pd.DataFrame({'Time':[0,1,2,3], 'Power':[1,3,3,7]})
#     div = drawing.get_plotly_string(df)
#     print(div)

# def run(address:str=None, p_max:float=1) -> str:
#     """Main calculation pipeline from address to plot."""

#     print(f"Started pipeline:\n")

#     print(f"Fetching weather data based on location '{address}' and factor '{p_max}' ...")
#     fdf = fetching.get_forecast_dataframe(address=address)
#     print(f"Fetched weather with {fdf.shape[0]} timesteps and {fdf.shape[1]} features\n")

#     print(f"Predicting power output ...")
#     pdf = inferencing.get_prediction_dataframe(df=fdf, p_max=p_max)
#     print(f"Predicted power with {pdf.shape[0]} timesteps\n")

#     print(f"Slicing data ...")
#     # x = pdf['date'].to_list()
#     x = pdf.index.tolist()
#     y = pdf['P_gen [kW]'].to_list()
#     print(f"Sliced {len(x)} time- and {len(y)} power-datapoints\n")

#     print(f"Finished pipeline:")
#     return x,y


# if __name__ == "__main__":
#     print("Just executed without function call")