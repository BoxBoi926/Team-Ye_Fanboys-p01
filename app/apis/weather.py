import urllib.parse as urlparse, urllib.request as urlrequest
import json

apiKey = "a591cc0b3ce141668cc142051211012"

ip = urlrequest.urlopen('https://ident.me').read().decode('utf8')

def getWeatherForCurrentLocation():
    url = "http://api.weatherapi.com/v1/current.json"
    params = {'key': apiKey, 'q': ip}

    urlParts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(urlParts[4]))
    query.update(params)
    
    urlParts[4] = urlparse.urlencode(query)
    siteData = urlrequest.urlopen(urlparse.urlunparse(urlParts))
    data = json.load(siteData)
    return data