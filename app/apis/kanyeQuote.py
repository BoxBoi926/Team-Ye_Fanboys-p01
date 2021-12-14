import urllib.request as urlrequest
import json

def getQuote():
    url = 'https://api.kanye.rest'

    headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
    request = urlrequest.Request(url, None, headers)
    siteData = urlrequest.urlopen(request)

    return json.load(siteData)['quote']