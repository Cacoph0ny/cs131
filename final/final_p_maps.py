##
#
#
##

APIKEY = 'ukod0Gz3hFtCy0gQoDnhEVw80wEewGVb'
APIURLBASE = 'http://www.mapquestapi.com/directions/v2/route?key='
APIURLFROM = '&from='
APIURLTO = '&to='

def test(key,base,urlfrom,to):
    userFrom = str(input('Test: '))
    userTo = str(input('Test: '))
    fullUrl = '%s%s%s%s%s%s' %(base, key, urlfrom, userFrom, to, userTo)
    print(fullUrl)

test(APIKEY, APIURLBASE, APIURLFROM, APIURLTO)
