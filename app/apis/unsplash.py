import urllib.parse as urlparse, urllib.request as urlrequest
import json
from flask import url_for

apiKey = 'q61EMMmSkbauKb5IHx-wFYIb6hct5J2-2t5qBdxCMdo'

def getUnsplashPhoto():
    try:
        url = "https://api.unsplash.com/photos/random?client_id="+apiKey

        params = {'orientation': 'landscape'}

        urlParts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(urlParts[4]))
        query.update(params)
        
        urlParts[4] = urlparse.urlencode(query)
        siteData = urlrequest.urlopen(urlparse.urlunparse(urlParts))
        data = json.load(siteData)
        return data['urls']['raw']
    except:
        return url_for('static', filename='images/fallbackBgImg.jpg')