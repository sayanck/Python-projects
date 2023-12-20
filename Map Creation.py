import folium


map = folium.Map(location=[51.5074, -0.1278], zoom_start=12)
folium.Marker(location=[51.5074, -0.1278], popup='London').add_to(map)

map.save('map.html')