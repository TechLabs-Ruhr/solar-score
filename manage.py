from data.core import fetching, drawing
from prediction.core import training, inferencing

def testfetching():
    print(fetching.mosmix_forecast().head())

def testinferencing():
    print(inferencing.dataframe.test())

def runpipeline(address:str=None) -> str:
    """Main calculation pipeline from address to plot."""

    print(f"Started pipeline\n")

    print(f"Fetching weather data based on '{address}'")
    fdf = fetching.get_forecast_dataframe(address=address)
    print(f"Fetched weather with {fdf.shape[0]} timesteps and {fdf.shape[1]} features\n")

    print(f"Predicting power output")
    pdf = inferencing.get_prediction_dataframe(df=fdf)
    print(f"Predicted power with {pdf.shape[0]} timesteps\n")

    print(f"Creating plot")
    div = drawing.get_plotly_string(df=pdf)
    print(f"Created plot with {len(div)} characters\n")

    print(f"Finished pipeline")
    return div


if __name__ == "__main__":
    print("Just executed without function call")