import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the data
df = pd.read_csv('data/festivals-processed.csv', sep=';')

# Filter the data
filtered_df = df[df["Sous-catégorie Musique CNM"] == "02- Musiques amplifiées ou électroniques"]

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

m.show_in_browser()

# Save the map to an HTML file
m.save('data/festivals_map.html')