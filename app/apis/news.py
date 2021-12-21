import urllib.request as urlrequest
import json

apiKey = "ZWgYdADsBPmpURWcbpTvGO4P8bsGtQMoriq9beSZTzYrADOE"

def getNews():
    try:
        url = 'https://api.currentsapi.services/v1/latest-news?country=US&apiKey='+apiKey
        siteData = urlrequest.urlopen(url)

        return json.load(siteData)['news']
    except Exception as issue:
        print("Error encountered while loading the news info.")
        print(issue)
        return {}
