import pandas as pd
from nypdarrestdata import numeric_analysis_of_arrests

def test_numeric_analysis_of_arrests():
    test_data = pd.DataFrame({
        'arrest_boro': ['K', 'M', 'Q', 'B', 'S', 'K', 'M'],
        'age_group': ['25-44', '<18', '45-64', '25-44', '18-24', '65+', '25-44'],
        'perp_sex': ['M', 'F', 'M', 'F', 'M', 'F', 'M'],
        'perp_race': ['BLACK', 'WHITE HISPANIC', 'ASIAN / PACIFIC ISLANDER', 'BLACK', 'BLACK HISPANIC', 'WHITE', 'WHITE'],
        'ofns_desc': ['ROBBERY', 'BURGLARY', 'FRAUD', 'ASSAULT', 'LARCENY', 'DRUGS', 'HOMICIDE']
    })

    result = numeric_analysis_of_arrests(test_data)
    assert isinstance(result, str), "The function did not return a string."
    assert result, "The function returned an empty string."
    for category in ['Arrests by Borough', 'Arrests by Age Group', 'Arrests by Gender', 'Arrests by Race', 'Top Charges']:
        assert category in result, f"Missing category in the result: {category}"

    print("Test passed: Numeric analysis returned a correctly formatted string.")

test_numeric_analysis_of_arrests()


