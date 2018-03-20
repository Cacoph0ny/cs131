##
# Tharin Dresher-Hurst
# hw03.py - Number to barcode
# 12 - 03 - 18
# Started work - tdh
# 19 - 03 - 18
# finishing printDigit - tdh
##

def printDigit(barCode):
    barCode=barCode[1:-6]
    barCode = barCode.replace(':','0')
    barCode = barCode.replace('|','1')
    for ii in range(0,5):
        tempNumber=barCode[(ii*5):(ii*5+5)]
        if tempNumber == '11000':
            print('0', end="")
        else:
            newNumber=(int(tempNumber[0]))*7+(int(tempNumber[1]))*4+(int(tempNumber[2]))*2+(int(tempNumber[3]))*1+(int(tempNumber[4]))*0
            print(newNumber, end="")

def printBarCode(zipCode):
    tempBar=[]
    for ii in range(0,5):
        tempNumber=zipCode[ii]
        if tempNumber == '0':
            tempBar.append('11000')
        elif tempNumber == '2':
            tempBar.append('00101')
        elif tempNumber == '4':
            tempBar.append('01001')
        elif tempNumber == '7':
            tempBar.append('10001')
        else:
            tempNumber=int(tempNumber)
            while tempNumber > 0:
                tempNumb=tempNumber//7
                tempBar.append(str(tempNumb))
                tempNumber -= tempNumb * 7
                tempNumber=tempNumber//4
                tempBar.append(str(tempNumb))
                tempNumber -= tempNumb * 4
                tempNumber=tempNumber//2
                tempBar.append(str(tempNumb))
                tempNumber -= tempNumb * 2
                tempNumber = tempNumber//1
                tempBar.append(str(tempNumb))
                tempNumber -= tempNumb * 1
    newBar="".join(tempBar)
    print(newBar)
    newBar = newBar.replace('0',':')
    newBar = newBar.replace('1','|')
    print(newBar)

def main():
    while True:
        userChoice=input("Do you have a zip code or a bar code(zip/bar)?\n")
        if userChoice == 'zip':
            userInputZip=str(input("Enter zip code: "))
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
