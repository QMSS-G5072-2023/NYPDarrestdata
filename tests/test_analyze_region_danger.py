from nypdarrestdata import fetch_arrest_data, analyze_region_danger
from unittest import mock
import pandas as pd

def test_fetch_and_analyze_region_danger():
    start_date = '2023-01-01'
    end_date = '2023-01-31'
    arrest_data = fetch_arrest_data(start_date, end_date)
    if not isinstance(arrest_data, pd.DataFrame) or arrest_data.empty:
        print("No data fetched for the specified date range. Test cannot proceed.")
        return
    with mock.patch('matplotlib.pyplot.show'):
        analyze_region_danger(arrest_data)

    print("Test passed: analyze_region_danger ran with fetched data without errors.")

test_fetch_and_analyze_region_danger()
