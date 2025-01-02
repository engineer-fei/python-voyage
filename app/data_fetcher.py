import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
NASA_API_KEY = os.getenv('NASA_API_KEY')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Local File - US Stock Market Data
def load_stock_data():
    try:
        data = pd.read_csv('data/us_stock_data.csv')
        return data
    except Exception as e:
        print(f"Error loading stock data: {e}")
        return None

# Local File - Global Development Data
def load_global_development_data():

    try:
        data = pd.read_csv('data/global_development_data.csv',header = 0, nrows=5000)
        #print(data)  # Print data to verify structure
        return data
    except Exception as e:
        print(f"Error loading global development data: {e}")
        return None


# API - NASA Open API

def fetch_nasa_api_data():
    endpoint=f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    print('endpoint:'+endpoint)

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        print(data)

        return pd.DataFrame([data])  # Wrapping in list to create single-row DataFrame
    except requests.exceptions.RequestException as e:
        print(f"NASA API request error: {e}")
        return None

# API - Alpha Vantage

def fetch_alpha_vantage_data(symbol="AAPL", api_key=ALPHA_VANTAGE_API_KEY):

    try:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(data, orient='index').reset_index()
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        return df
    except requests.exceptions.RequestException as e:
        print(f"Alpha Vantage API request error: {e}")
        return None
