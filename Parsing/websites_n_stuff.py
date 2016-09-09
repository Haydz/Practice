#https://docs.python.org/2/howto/urllib2.html

import urllib2
req = urllib2.Request('http://www.google.com')
response = urllib2.urlopen(req)
print response.read()

#encoding is done from URLLIB

import urllib
url = 'http://www.test.com'

values = {'cookie': 'test', 'location' : 'farud'}

#just playing with fake request data
data = urllib.urlencode(values)
req2 = urllib2.Request(url, data)
response = urllib2.urlopen(req2)
page2 = response.read()
print page2