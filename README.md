# KML to Interactive Map Converter

This Python script converts KML (Keyhole Markup Language) files into an interactive map using the Folium library. It parses KML files, extracts geographical data, and creates an HTML file that displays the data on an interactive map.

## Prerequisites

Before running the script, ensure that you have the following prerequisites installed:

- Python 3.x
- Folium library (`pip install folium`)

## Usage

1. Clone or download this repository to your local machine.
2. Place your KML files in a folder of your choice (e.g., `/content/kml`).
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```shell
   python script.py 

Replace `script.py` with the actual name of the script if it's different.

After running the script, it will generate an interactive map and save it as `plot_map.html` in the current directory.

## Configuration
You can customize the behavior of the script by modifying the following parameters:

`kml_folder`: Set the path to the folder containing your KML files.
`Map settings`: You can adjust the initial map settings, such as zoom level, tile providers (Google, OpenStreetMap), and more in the script.

## Example
The script reads KML files from the specified folder, extracts polygon and line data, calculates average coordinates, and displays them on an interactive map. It also provides tooltips with descriptions if available in the KML.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Folium: https://python-visualization.github.io/folium/
ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html
Feel free to contribute to this project by submitting issues or pull requests.

Happy mapping!
