import requests
import json
# Just a generated code maybe for use later
# Replace with your actual access token and activity ID
access_token = 'dc140e91c376b4b1a599381d541a3c9f447d737b'
activity_id = '12515758477'

# Fetch activity details
response = requests.get(
    f'https://www.strava.com/api/v3/activities/{activity_id}',
    headers={'Authorization': f'Bearer {access_token}'}
)

if response.status_code == 200:
    activity_data = response.json()
    print(json.dumps(activity_data, indent=4))  # Print activity data for debugging

    # Extract the GPS coordinates
    if 'map' in activity_data and 'polyline' in activity_data['map']:
        polyline = activity_data['map']['polyline']
        print(f"Polyline: {polyline}")
    else:
        print("No GPS data found in the activity.")
else:
    print(f"Failed to fetch activity details: {response.status_code}, {response.text}")

def decode_polyline(polyline_str):
    """Decode a Google Maps encoded polyline into a list of (lat, lon) tuples."""
    poly = []
    index = 0
    length = len(polyline_str)
    lat = 0
    lon = 0

    while index < length:
        result = 0
        shift = 0
        while True:
            b = ord(polyline_str[index]) - 63
            result |= (b & 0x1f) << shift
            index += 1
            if b < 0x20:
                break
            shift += 5
        dlat = ~(result >> 1) if (result & 1) else result >> 1
        lat += dlat

        result = 0
        shift = 0
        while True:
            b = ord(polyline_str[index]) - 63
            result |= (b & 0x1f) << shift
            index += 1
            if b < 0x20:
                break
            shift += 5
        dlon = ~(result >> 1) if (result & 1) else result >> 1
        lon += dlon

        poly.append((lat / 1E5, lon / 1E5))

    return poly

# Example usage of decode_polyline
if 'polyline' in activity_data['map']:
    decoded_points = decode_polyline(activity_data['map']['polyline'])
    print("Decoded GPS Points:", decoded_points)

import folium

# Create a map centered at the first point
m = folium.Map(location=decoded_points[0], zoom_start=13)

# Add a polyline to the map
folium.PolyLine(decoded_points, color="blue", weight=5, opacity=0.7).add_to(m)

# Add markers for each point (optional)
for point in decoded_points:
    folium.Marker(location=point).add_to(m)

# Save map to an HTML file
m.save("strava_activity_map.html")