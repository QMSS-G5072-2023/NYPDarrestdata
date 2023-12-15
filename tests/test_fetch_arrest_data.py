from nypdarrestdata import fetch_arrest_data
import os

def test_fetch_arrest_data():
    start_date = '2022-01-01'
    end_date = '2022-01-30'
    
    data = fetch_arrest_data(start_date, end_date)

    if data.empty:
        print("Test failed: No data fetched.")
    else:
        print("Test passed: Data fetched successfully.")

test_fetch_arrest_data()



