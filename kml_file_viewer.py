import os
import xml.etree.ElementTree as ET
import folium
import shutil

kml_folder = '/content/kml'

def create_kmlmaps(kml_folder):
    latitudes = []
    longitudes = []

    m = folium.Map(location=[0, 0], zoom_start=13, tiles='http://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', attr='Google Normal', name='Normal', max_native_zoom=20, max_zoom=20)

    for filename in os.listdir(kml_folder):
        if filename.endswith('.kml'):
            kml_path = os.path.join(kml_folder, filename)

            tree = ET.parse(kml_path)
            root = tree.getroot()

            features = []
            for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
                geometry_element = placemark.find('.//{http://www.opengis.net/kml/2.2}Polygon') or placemark.find('.//{http://www.opengis.net/kml/2.2}LineString')
                if geometry_element is not None:
                    coordinates = geometry_element.find('.//{http://www.opengis.net/kml/2.2}coordinates').text.strip()
                    coordinates = [list(map(float, coord.split(','))) for coord in coordinates.split()]

                    description_element = placemark.find('.//{http://www.opengis.net/kml/2.2}description')
                    description_text = description_element.text.strip() if description_element is not None else ''

                    lats = [coord[1] for coord in coordinates]
                    lons = [coord[0] for coord in coordinates]
                    avg_lat = sum(lats) / len(lats)
                    avg_lon = sum(lons) / len(lons)

                    latitudes.append(avg_lat)
                    longitudes.append(avg_lon)

                    properties = {"description": description_text} if description_text else {}

                    feature = {
                        "type": "Feature",
                        "properties": properties,
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [coordinates]
                        }
                    }
                    features.append(feature)

            geojson_data = {
                "type": "FeatureCollection",
                "features": features
            }

            folium.GeoJson(
                geojson_data,
                name=filename.split('.')[0],
                tooltip=folium.GeoJsonTooltip(fields=['description'], labels=False) if any(feature["properties"].get("description") for feature in features) else None
            ).add_to(m)

    if latitudes and longitudes:
        map_center = [sum(latitudes) / len(latitudes), sum(longitudes) / len(longitudes)]
        m.location = map_center

    folium.TileLayer(tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', attr='OpenStreetMap', name='OSM', max_native_zoom=20, max_zoom=20).add_to(m)
    folium.TileLayer(tiles='http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', attr='Google Satellite', name='Satellite', max_native_zoom=20, max_zoom=20).add_to(m)
    folium.TileLayer(tiles='http://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Hybrid', name='Hybrid', max_native_zoom=20, max_zoom=20).add_to(m)

    folium.LayerControl().add_to(m)

    map_file = 'plot_map.html'
    m.save(map_file)

    print(f"Map saved to {map_file}")

create_kmlmaps(kml_folder)
