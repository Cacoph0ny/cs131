##
# Tharin Dresher-Hurst
# final_p_out.py
# 16 - 05 - 18
# started and finished - tdh
##

import final_p_maps

class MasterOutput:
    def __init__(self, data, data2):
        self.__data = data
        self.__data2 = data2
    def printSteps(self):
        steps = int(input(""))
        stepsList = ['DIRECTIONS','TOTALTIME','TOTALDISTANCE','LATLONG','ELEVATION']
        for ii in range(0,steps):
            print(stepsList[ii])
        return steps
    def printDir(self):
        directions = final_p_maps.printDir(self.__data)
        for ii in range(len(directions)):
            print(directions[ii])
        print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMapContributors.")
    def printTime(self):
        time = final_p_maps.getTime(self.__data)
        print("Time: %d minutes" %((time/60)))
    def printDist(self):
        dist = final_p_maps.getDistance(self.__data)
        print(dist)
    def printLatLng(self):
        latLng = final_p_maps.getLatLong(self.__data2)
        print(latLng)
