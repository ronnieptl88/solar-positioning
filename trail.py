import googlemaps
import folium
import pvlib
import datetime

# Replace with your Google Maps API key
API_KEY = 'YOUR_API_KEY'

# Initialize the Google Maps API client
gmaps = googlemaps.Client(key='AIzaSyAftRNXU6CGaRywPKe_z-vvEhLspDwhgVE')

# Replace with the address you want to mark
address = '1600 Amphitheatre Parkway, Mountain View, CA'

# Geocode the address to get latitude and longitude
geocode_result = gmaps.geocode(address)
location = geocode_result[0]['geometry']['location']
latitude = location['lat']
longitude = location['lng']

# Current date and time
current_datetime = datetime.datetime.now()

# Solar position calculations
tz = 'UTC'  # Set the timezone
solar_position = pvlib.solarposition.get_solarposition(
    current_datetime, latitude, longitude, method='nrel_numpy'
)

# Create a map centered at the marked location
m = folium.Map(location=[latitude, longitude], zoom_start=15)

# Add a marker for the marked location
folium.Marker([latitude, longitude], popup=address).add_to(m)

# Add solar position information to the marker's popup
popup_content = f"Time: {current_datetime}<br>Solar Azimuth: {solar_position['azimuth'][0]}°<br>Solar Elevation: {solar_position['elevation'][0]}°"
folium.Marker([latitude, longitude], popup=popup_content).add_to(m)

# Save the map to an HTML file
m.save('solar_position_map.html')
