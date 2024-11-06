from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Load the data
    df = pd.read_csv('data/festivals-processed.csv', sep=';')

    # Filter the data
    filtered_df = df.copy()

    # Get unique years for the dropdown
    unique_years = sorted(filtered_df['Année de création du festival'].dropna().unique())

    # Apply year filter if provided
    year = request.form.get('year')
    if year:
        filtered_df = filtered_df[filtered_df['Année de création du festival'] == int(year)]

    # Convert lat and lon to numeric
    filtered_df["lat"] = pd.to_numeric(filtered_df["lat"])
    filtered_df["lon"] = pd.to_numeric(filtered_df["lon"])

    # Create a map centered around France
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

    # Add points to the map
    marker_cluster = MarkerCluster().add_to(m)
    for idx, row in filtered_df.iterrows():
        folium.Marker(location=[row['lat'], row['lon']], tooltip=row['Nom du festival'],
                      popup=f"Web site: {row['Site internet du festival']} \n \n Creation year: {row['Année de création du festival']}").add_to(marker_cluster)

    # Save the map to an HTML file
    map_path = 'templates/festivals_map.html'
    m.save(map_path)

    return render_template('index.html', map_html=m._repr_html_(), year=year, unique_years=unique_years)

if __name__ == '__main__':
    app.run(debug=True)


