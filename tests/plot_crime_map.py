import pandas as pd
from nypdarrestdata import plot_crime_map

def test_plot_crime_map():
   
    test_data = pd.DataFrame({
        'latitude': [40.7128, None],  
        'longitude': [-74.0060, None],
        'arrest_date': ['2023-01-01T00:00:00.000', '2023-01-02T00:00:00.000'],
        'perp_race': ['WHITE', 'BLACK'],
        'age_group': ['25-44', '<18'],
        'perp_sex': ['M', 'F'],
        'ofns_desc': ['BURGLARY', 'ROBBERY']
    })

  
    crime_map = plot_crime_map(test_data)
    assert crime_map is not None, "Map object is not created."
    assert len(crime_map._children) - 1 == 1, "Map does not contain the correct number of markers."

    print("Test passed: Crime map generated with correct number of markers.")

test_plot_crime_map()
