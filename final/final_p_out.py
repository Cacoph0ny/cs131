##
# Tharin Dresher-Hurst
# final_p_out.py
# 16 - 05 - 18
# started and finished - tdh
##

import final_p_maps

class MasterOutput:
    def __init__(self, data, data2, data3):
        self.__data = data
        self.__data2 = data2
        self.__data3 = data3
    def printSteps(self):
        steps = int(input(""))
        stepsList = ['DIRECTIONS','TOTALTIME','TOTALDISTANCE','LATLONG']
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
        print("Distance: %.2f miles" %(dist))
    def printLatLng(self):
        latLng = final_p_maps.getLatLong(self.__data2)
        print("LATLONG")
        for ii in range(len(latLng)):
            temp1 = (latLng[ii]['lat'])
            if temp1 <= 90:
                temp1d = 'N'
            else:
                temp1d = 'S'
            print("%.2f %s" %((abs(temp1)), temp1d))
            temp2 = (latLng[ii]['lng'])
            if temp2 <= 90:
                temp2d = 'E'
            else:
                temp2d = 'W'
            print("%.2f %s" %((abs(temp2)), temp2d))
    def printElevation(self):
        elevation = final_p_maps.getElevation(self.__data3)
        print(elevation)
