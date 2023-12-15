import folium
from datetime import datetime
import pandas as pd

def plot_crime_map(data):
"""
Generates an interactive crime map using Folium based on arrest data.
m is the 'latitude' and 'longtitude' of NYC
This function iterates over a provided DataFrame and plots points on the map corresponding to the geographical location of each crime.
Additional information about each crime, such as the date, race, age group, sex, and charges, is displayed in a popup on the map.
In order to execute furthur it is better to use 'data_fetching' function to utilize the data and print out the map.
"""

    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
    for idx, row in data.iterrows():
        if not pd.isna(row['latitude']) and not pd.isna(row['longitude']):
            date_formatted = datetime.strptime(row['arrest_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            popup_text = f"Date: {date_formatted}<br>"
            popup_text += f"Race: {row['perp_race']}<br>"
            popup_text += f"Age Group: {row['age_group']}<br>"
            popup_text += f"Sex: {row['perp_sex']}<br>"
            popup_text += f"Charges: {row['ofns_desc']}"

            popup = folium.Popup(popup_text, max_width=300)

            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                popup=popup
            ).add_to(m)
    return m

