##
# Tharin Dresher-Hurst
# Rabbit.py
# 26 - 02 - 2018
# Created user input function - TDH
# 02 - 03 - 2018
# Restarted the whole thing because first idea wasn't working - TDH
##

def main():
    wolfPop=float(input("Starting wolf population:\t"))
    rabbitPop=float(input("Starting rabbit population:\t"))
    grassArea=float(input("Starting grass area:\t\t"))
    wolfGrow=float(input("Wolf growth rate annually:\t"))
    rabbitGrow=float(input("Rabbit growth rate annually:\t"))
    grassGrow=float(input("Grass growth rate annually:\t"))
    wolfPopSmall=wolfPop
    wolfPopBig=wolfPop
    rabbitPopSmall=rabbitPop
    rabbitPopBig=rabbitPop
    wolfSmallCount=0
    wolfBigCount=0
    rabbitSmallCount=0
    rabbitBigCount=0
    counter=0
    wolfCount=0
    while counter <= 20:
        if counter == 0:
            print("Year\t","Wolf Population\t","Rabbit Population\t","Grass Area")
            print("\n%d\t %.0f\t\t\t %.0f\t\t\t %.2f" %(counter,wolfPop,rabbitPop,grassArea))
            counter += 1
        else:
            grassArea= (grassArea * (1 + grassGrow/100) - (rabbitPop * 1.2))
            rabbitPop= (rabbitPop * (1 + rabbitGrow/100) - (wolfPop*50))//1
            if rabbitPop > rabbitPopBig:
                rabbitPopBig = rabbitPop
                rabbitBigCount = counter
            if rabbitPop < rabbitPopSmall:
                rabbitPopSmall = rabbitPop
                rabbitSmallCount = counter
            if wolfCount == 5:
                wolfPop = (wolfPop/2)//1
                wolfCount = 1
                if wolfPop > wolfPopBig:
                    wolfPopBig = wolfPop
                    wolfBigCount = counter
                if wolfPop < wolfPopSmall:
                    wolfPopSmall = wolfPop
                    wolfSmallCount = counter
            else:
                wolfPop = (wolfPop * (1+(wolfGrow/100)))//1
                wolfCount += 1
                if wolfPop > wolfPopBig:
                    wolfPopBig = wolfPop
                    wolfBigCount = counter + 1
                if wolfPop < wolfPopSmall:
                    wolfPopSmall = wolfPop
                    wolfSmallCount = counter + 1
            print("%d\t %.0f\t\t\t %.0f\t\t\t %.2f" %(counter,wolfPop,rabbitPop,grassArea))
            counter += 1
    print("Wolf population was minimum at %d in the year %d" %(wolfPopSmall, wolfSmallCount))
    print("Wolf population was maximum at %d in the year %d" %(wolfPopBig, wolfBigCount))
    print("Rabbit population was minimum at %d in the year %d" %(rabbitPopSmall, rabbitSmallCount))
    print("Rabbit population was maximum at %d in the year %d" %(rabbitPopBig, rabbitBigCount))


main()
