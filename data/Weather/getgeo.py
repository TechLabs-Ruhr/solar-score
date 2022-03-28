import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os

def get_long_lat(address):
    """
    Gives back dict with latitude and longitude value of an adress. Request made via mapquest.

        Parameters:
            address (str): address of which latidude and longitude are requested

        Returns:
            dict with latidude and longitude of address
    """    

    #input: address and API key
    load_dotenv()
    parameters = {
        "key": os.getenv("api_key"),
        "location": address
    }
    #respone from mapquest
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    data = response.text
    dataJ = json.loads(data)['results']
    #save latitude and longitude value in dict
    dict_geo={}
    lat = (dataJ[0]['locations'][0]['latLng']['lat'])
    dict_geo["lat"]=lat
    lng = (dataJ[0]['locations'][0]['latLng']['lng'])
    dict_geo["lng"]=lng
    return dict_geo


