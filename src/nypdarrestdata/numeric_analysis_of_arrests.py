from tabulate import tabulate

def numeric_analysis_of_arrests(data):
"""
Analyzes arrest data and returns a formatted string representation of various arrest statistics.
This function takes a dataset of arrest records and performs a numeric analysis on different categories 
such as borough, age group, gender, race, and offense descriptions. It calculates the count of arrests for each category.
The top 5 charges are also included in the analysis. The results are formatted as a string with each category presented in a 
tabular format."""

    borough_names = {'K': 'Brooklyn', 'M': 'Manhattan', 'Q': 'Queens', 'B': 'Bronx', 'S': 'Staten Island'}
    analysis_categories = {
        'Arrests by Borough': data['arrest_boro'].map(borough_names).value_counts(),
        'Arrests by Age Group': data['age_group'].value_counts(),
        'Arrests by Gender': data['perp_sex'].value_counts(),
        'Arrests by Race': data['perp_race'].value_counts(),
        'Top Charges': data['ofns_desc'].value_counts().head(5)
        }

    formatted_output = ""
    for category, counts in analysis_categories.items():
        formatted_output += f"{category}:\n"
        formatted_output += tabulate(counts.items(), headers=['Category', 'Count'], tablefmt='grid')
        formatted_output += "\n\n"

    return formatted_output
