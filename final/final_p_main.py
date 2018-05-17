##
# Tharin Dresher-Hurst
# final_p_main.py
# 16 - 05 - 18
# started and finished - tdh
##

import final_p_out
import final_p_maps

def main():
    numberInputs = (int(input("")))-1
    mainData, geoData, eleData = final_p_maps.cleanData(numberInputs)
    Outputs = final_p_out.MasterOutput(mainData, geoData, eleData)
    steps = Outputs.printSteps()
    if steps >= 1:
        Outputs.printDir()
    if steps >= 2:
        Outputs.printTime()
    if steps >= 3:
        Outputs.printDist()
    if steps >= 4:
        Outputs.printLatLng()
    if steps >= 5:
        Outputs.printElevation()

main()
