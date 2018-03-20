##
# Tharin Dresher-Hurst
# hw03.py - Number to barcode
# 12 - 03 - 18
# Started work - tdh
##

def printDigit(barCode):
    barCode=barCode[1:-6]
    barCode = barCode.replace(':','0')
    barCode = barCode.replace('|','1')
    for ii in range(0,5):
        tempNumber=barCode[(ii*5):(ii*5+5)]
        tempNumber=((tempNumber[0])*7+(tempNumber[1])*4+(tempNumber[2])*2+(tempNumber[3])*1+(tempNumber[4])*0)
        print(tempNumber , end='')
        break

def printBarCode(zipCode):
    break

def main():
    while True:
        userChoice=input("Do you have a zip code or a bar code(zip/bar)?\n")
        if userChoice == 'zip':
            userInputZip=int(input("Enter zip code: "))
            printBarCode(userInputZip)
            break
        elif userChoice == 'bar':
            userInputBar=str(input("Enter bar code: "))
            if userInputBar.startswith('|') and userInputBar.endswith('|'):# and len(userInputBar) == 32:
                printDigit(userInputBar)
                break
            else:
                print("error")
        else:
            print("Invalid Input")

main()
