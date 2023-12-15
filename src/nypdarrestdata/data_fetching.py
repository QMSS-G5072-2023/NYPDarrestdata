import requests
import pandas as pd

def fetch_arrest_data(start_date, end_date):
"""
Fetches arrest data between two dates from the New York Police Department database.
Date should be written in yyyy-mm-dd format, limit is set as 30000 but it can be changed by users' preferences.
"""
    url = "https://data.cityofnewyork.us/resource/uip8-fykc.json"
    params = {
        "$where": f"arrest_date between '{start_date}' and '{end_date}'",
        "$limit": 5000  # Adjust as necessary, if the number is too high, map function crashes. 
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
