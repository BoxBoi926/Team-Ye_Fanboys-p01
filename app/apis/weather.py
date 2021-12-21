import urllib.parse as urlparse, urllib.request as urlrequest
import json
from apis import getIpAddress

apiKey = "a591cc0b3ce141668cc142051211012"

ip = getIpAddress.getIp()

def getWeatherForCurrentLocation():
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {'key': apiKey, 'q': ip}

        urlParts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(urlParts[4]))
        query.update(params)
        
        urlParts[4] = urlparse.urlencode(query)
        siteData = urlrequest.urlopen(urlparse.urlunparse(urlParts))
        data = json.load(siteData)
        return data
    except Exception as issue:
        print('Unable to get weather location')
        print(issue)
        return {}

# example formatting:

# {'location': {'name': 'Washington Heights', 'region': 'New York', 'country': 'United States of America', 'lat': 40.85, 'lon': -73.94, 'tz_id': 'America/New_York', 'localtime_epoch': 1639617025, 'localtime': '2021-12-15 20:10'}, 'current': {'last_updated_epoch': 1639612800, 'last_updated': '2021-12-15 19:00', 'temp_c': 11.1, 'temp_f': 52.0, 'is_day': 0, 'condition': {'text': 'Overcast', 'icon': '//cdn.weatherapi.com/weather/64x64/night/122.png', 'code': 1009}, 'wind_mph': 0.0, 'wind_kph': 0.0, 'wind_degree': 164, 'wind_dir': 'SSE', 'pressure_mb': 1031.0, 'pressure_in': 30.43, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 71, 'cloud': 100, 'feelslike_c': 9.4, 'feelslike_f': 48.9, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 1.0, 'gust_mph': 13.6, 'gust_kph': 22.0}}