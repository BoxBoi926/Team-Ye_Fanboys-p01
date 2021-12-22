import urllib.request as urlrequest

def getIp():
    try:
        return urlrequest.urlopen('https://ident.me').read().decode('utf8')
    except Exception as issue:
        print("No location found.")
        print(issue)
        return ''