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
GEOCODEURL = 'http://www.mapquestapi.com/geocoding/v1/batch?key='
GEOCODEFILL = '&location='
LATLONGURL = 'http://open.mapquestapi.com/elevation/v1/profile?key'
LATLONGFILL = '&shapeFormat=raw&latLngCollection='

def buildUrl(key,base,urlfrom,to, inputs, basegeo, geofill):
    userFrom = str(input(''))
    tempFrom = userFrom.replace(" ","+")
    fullUrl = '%s%s%s%s' %(base, key, urlfrom, tempFrom)
    geoCodeUrl = '%s%s%s%s' %(basegeo, key, geofill, tempFrom)
    for ii in range(inputs):
        userTo = str(input(''))
        tempTo = userTo.replace(" ","+")
        fullUrl = '%s%s%s' %(fullUrl, to, tempTo)
        geoCodeUrl = '%s%s%s' %(geoCodeUrl, geofill, tempTo)
    print('\n')
    return fullUrl, geoCodeUrl

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

def getLatLong(geoData):
    finalList = []
    geoLat = geoData['results']
    for ii in geoLat:
        for oo in ii['locations']:
            finalList.append(oo['latLng'])
    return finalList

def getElevationUrl(geoData, key, base, fill):
    latLngList = getLatLong(geoData)
    url = '%s%s%s' %(base, key, fill)
    for ii in range(len(latLngList)):
        temp1 = (str(latLngList[0]['lat']))
        temp2 = (str(latLngList[0]['lng']))
        temp3 = (str(latLngList[1]['lat']))
        temp4 = (str(latLngList[1]['lng']))
        url = '%s%s,%s,%s,%s' %(url, temp1, temp2, temp3, temp4)
    return url

def getElevationData(url):
    data = urlopen('%s' %(url))
    eleData = json.loads(data.read())
    return eledata

def getElevation(eleData):
    finalList = []
    elevation = eleData['elevationProfile']
    for ii in elevation:
        finalList.append(ii['height'])
    return finalList

def getDistance(dataMap):
    distance = dataMap['route']['distance']
    return distance

def getTime(dataMap):
    time = dataMap['route']['time']
    return time

def cleanData(inputs):
    urlFinal, geoCodeUrl = buildUrl(APIKEY, APIURLBASE, APIURLFROM, APIURLTO, inputs, GEOCODEURL, GEOCODEFILL)
    mapData = {}
    mapData = dataFormat(urlFinal)
    geoData = {}
    geoData = dataFormat(geoCodeUrl)
    urlEle = getElevationUrl(geoData, APIKEY, GEOCODEURL, GEOCODEFILL)
    eleData = {}
    eleData = dataFormat(urlEle)
    return mapData, geoData, eleData
