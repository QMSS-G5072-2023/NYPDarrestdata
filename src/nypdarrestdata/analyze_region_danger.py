import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def analyze_region_danger(data):
    """
    Analyzes and visualizes arrest data by different demographic and crime categories in New York City boroughs.
    This function first standardizes race categories in the dataset, filters out unknown race entries, and 
    remaps borough codes to their names. It then generates a bar plot showing the number of arrests in each 
    NYC borough. Additionally, for each borough, the function provides detailed visualizations of the 
    distribution of arrests by age group, gender, race, and the top three charges.
    The function relies on another function, `plot_distribution`, for generating individual distribution plots.
    """

    race_mapping = {
        'BLACK': 'Black',
        'BLACK HISPANIC': 'Hispanic',
        'WHITE': 'White',
        'WHITE HISPANIC': 'Hispanic',
        'ASIAN / PACIFIC ISLANDER': 'Asian',
        'AMERICAN INDIAN/ALASKAN NATIVE': 'Native American',
    }

    data['perp_race'] = data['perp_race'].map(race_mapping)
    data = data[data['perp_race'] != 'UNKNOWN']
    borough_names = {'K': 'Brooklyn', 'M': 'Manhattan', 'Q': 'Queens', 'B': 'Bronx', 'S': 'Staten Island'}
    danger_by_region = data['arrest_boro'].value_counts().rename(index=borough_names)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=danger_by_region.index, y=danger_by_region.values)
    plt.title("Number of Arrest Cases by NYC Borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of Arrests")
    plt.show()

    for region in danger_by_region.index:
        print(f"\nAnalysis for {region}:")
        region_data = data[data['arrest_boro'].map(borough_names) == region]
        plot_distribution(region_data, 'age_group', f"Age Group Distribution in {region}")
        plot_distribution(region_data, 'perp_sex', f"Sex Distribution in {region}")
        plot_distribution(region_data, 'perp_race', f"Race Distribution in {region}")
        plot_distribution(region_data, 'ofns_desc', f"Top 3 Charges in {region}", limit=3)

def plot_distribution(data, column, title, limit=None):
    if limit:
        counts = data[column].value_counts().head(limit)
    else:
        counts = data[column].value_counts()

    plt.figure(figsize=(10, 4))
    sns.barplot(x=counts.index, y=counts.values)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()
