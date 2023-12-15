import folium
import pandas as pd

def plot_crime_map(data):
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)

    for idx, row in data.iterrows():
        if not pd.isna(row['latitude']) and not pd.isna(row['longitude']):
            popup_text = f"Date: {row['arrest_date']}<br>"
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

