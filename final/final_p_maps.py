##
# Tharin Dresher-Hurst
# fial_p_maps.py
# XX - 05 - 18
# started playing with url opeing and getting the dataMap - tdh
# 16 - 05 - 18
# finished up the fuctions and made the names better
##

from urllib.request import urlopen
import json

APIKEY = 'ukod0Gz3hFtCy0gQoDnhEVw80wEewGVb'
APIURLBASE = 'http://www.mapquestapi.com/directions/v2/route?key='
APIURLFROM = '&from='
APIURLTO = '&to='

def buildUrl(key,base,urlfrom,to, inputs):
    userFrom = str(input(''))
    tempFrom = userFrom.replace(" ","+")
    fullUrl = '%s%s%s%s' %(base, key, urlfrom, tempFrom)
    for ii in range(inputs):
        userTo = str(input(''))
        tempTo = userTo.replace(" ","+")
        fullUrl = '%s%s%s' %(fullUrl, to, tempTo)
    print('\n')
    return fullUrl

def dataFormat(URL):
    data = urlopen('%s' %(URL))
    mapData = json.loads(data.read())
    return mapData

def printDir(dataMap):
    finalList = []
    steps = dataMap['route']['legs']
    for ii in steps:
        for oo in ii['maneuvers']:
            finalList.append(oo['narrative'])
    return finalList

def getDistance(dataMap):
    distance = dataMap['route']['distance']
    return distance

def getTime(dataMap):
    time = dataMap['route']['time']
    return time

def cleanData(inputs):
    urlFinal = buildUrl(APIKEY, APIURLBASE, APIURLFROM, APIURLTO, inputs)
    mapData = {}
    mapData = dataFormat(urlFinal)
    return mapData
