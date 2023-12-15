import requests
import pandas as pd

def fetch_arrest_data(start_date, end_date):
    url = "https://data.cityofnewyork.us/resource/8h9b-rp9u.json"
    params = {
        "$where": f"arrest_date between '{start_date}' and '{end_date}'",
        "$limit": 10000  # Adjust as necessary
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = pd.DataFrame(response.json())      
        data['arrest_date'] = pd.to_datetime(data['arrest_date']).dt.strftime('%Y-%m-%d')
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
