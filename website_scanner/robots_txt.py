import urllib2
import io


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    print path + "robots.txt"
    req = urllib2.Request(url=path + "robots.txt", data=None)
    data = urllib2.urlopen(req)
    #data = io.TextIOWrapper(req, encoding='utf-8')
    # return data#.read()
    # return req.read()
    return data.read()


#print get_robots_txt('https://reddit.com')
