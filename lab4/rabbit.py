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
    grassArea=float(input("Starting grass area (in square yards):\t"))
    wolfGrow=float(input("Wolf growth rate annually (in percent):\t"))
    rabbitGrow=float(input("Rabbit growth rate annually (in percent):\t"))
    grassGrow=float(input("Grass growth rate annually (in percent):\t"))
    wolfPopSmall=wolfPop
    wolfPopBig=wolfPop
    rabbitPopSmall=0
    rabbitPopBig=0
    counter=0
    wolfCount=0
    while counter <= 20:
        if counter == 0:
            print("Year\t","Wolf Population\t","Rabbit Population\t","Grass Area")
            print("\n%d\t %.0f\t\t\t %.0f\t\t\t %.2f" %(counter,wolfPop,rabbitPop,grassArea))
            counter += 1
        else:
            grassArea= (grassArea * (1 + grassGrow/100) - (rabbitPop * 1.2))//1
            rabbitPop= (rabbitPop * (1 + rabbitGrow/100) - (wolfPop*50))//1
            if wolfCount == 5:
                wolfPop /= 2
                wolfCount = 1
            else:
                wolfPop = (wolfPop * (1+(wolfGrow/100)))//1
                wolfCount += 1
            print("%d\t %.0f\t\t\t %.0f\t\t\t %.2f" %(counter,wolfPop,rabbitPop,grassArea))
            counter += 1

main()
