import urllib.request as urlrequest
import json

apiKey = "api_key"

def getNews():
    '''Grabs news from the news api.'''
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='+apiKey
        siteData = urlrequest.urlopen(url)

        return json.load(siteData)['articles']
    except Exception as issue:
        print("Error encountered while loading the news info.")
        print(issue)
        return []