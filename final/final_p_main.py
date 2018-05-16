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
    mainData = final_p_maps.cleanData(numberInputs)
    Outputs = final_p_out.MasterOutput(mainData)
    Outputs.printDir()
    Outputs.printTime()

main()
