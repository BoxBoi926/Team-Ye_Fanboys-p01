import urllib.request as urlrequest
import json

def getQuote():
    url = 'api.kanye.rest'

    siteData = urlrequest.urlopen(url)

    print(json.load(siteData))

getQuote()