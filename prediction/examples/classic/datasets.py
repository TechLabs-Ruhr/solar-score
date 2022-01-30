import statsmodels.datasets.co2 as co2

def get_co2():
    """Small wrapper for getting and cleaning the CO2 data from statsmodels datasets."""
    
    co2_data = co2.load().data
    co2_data = co2_data.fillna(co2_data.interpolate())

    return co2_data


if __name__ == "__main__":
    print()