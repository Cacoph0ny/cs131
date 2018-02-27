##
# Tharin Dresher-Hurst
# Rabbit.py
# 26 - 02 - 2018
# Created user input function
#
##

def userInputs():
    tempList=[]
    wolfPop=float(input("Starting wolf population:\t"))
    rabbitPop=float(input("Starting rabbit population:\t"))
    grassArea=float(input("Starting grass area (in square yards):\t"))
    wolfGrowth=float(input("Wolf growth rate annually (in percent):\t"))
    rabbitGrowth=float(input("Rabbit growth rate annually (in percent):\t"))
    grassGrowth=float(input("Grass growth rate annually (in percent):\t"))
    finalList=tempList.extend((wolfPop, rabbitPop, grassArea, wolfGrowth, rabbitGrowth, grassGrowth))
    return finalList

def wolfPopCalc(pop,grow):
    wolfTemp=pop*(1+(grow/100))
    return (wolfTemp//1)

def rabbitPopCalc(popR,popW,grow):
    rabbitTemp=popR*(1+(grow/100))-(popW*50)
    return (rabbitTemp//1)

def grassAreaCalc(grass,grow,pop):
    grassTemp=grass*(1+(grow/100))-(pop*1.2)
    return (grassTemp)

def main():
    counter=0
    while counter != 20:
        
