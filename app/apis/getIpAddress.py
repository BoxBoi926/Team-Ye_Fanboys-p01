import urllib.request as urlrequest

def getIp():
    '''Grabs the externally facing IP address for detecting user location.'''
    try:
        return urlrequest.urlopen('https://ident.me').read().decode('utf8')
    except Exception as issue:
        print("No location found.")
        print(issue)
        return ''