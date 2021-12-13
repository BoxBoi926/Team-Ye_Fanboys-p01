import urllib.parse as urlparse, urllib.request as urlrequest
from urllib.parse import urlencode
import json, socket

apiKey = "ZWgYdADsBPmpURWcbpTvGO4P8bsGtQMoriq9beSZTzYrADOE"

def getNews():
    url = 'https://api.currentsapi.services/v1/latest-news?country=US&apiKey='+apiKey
    siteData = urlrequest.urlopen(url)

    return json.load(siteData)['news']

getNews()