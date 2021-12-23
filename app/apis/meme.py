import urllib.request as urlrequest
import json

def getMeme(returnNum: int = 10, resource: str = "kanye"):
    try:
        url = "https://meme-api.herokuapp.com/gimme/"+resource+"/"+str(returnNum)
        siteData = urlrequest.urlopen(url)

        return json.load(siteData)['memes']
    except Exception as issue:
        print("Error encountered while loading memes.")
        print(issue)
        return {}

print(getMeme())