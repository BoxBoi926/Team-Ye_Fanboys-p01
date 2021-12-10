import urllib.request as request
import json, socket

apiKey = "a591cc0b3ce141668cc142051211012"

def getWeatherForCurrentLocation():
    url = "http://api.weatherapi.com/v1/current.json"
    siteData = request.urlopen(url)
    params = {'key': apiKey, 'q': socket.gethostname()}
    