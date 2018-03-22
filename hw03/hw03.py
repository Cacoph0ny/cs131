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
        elif tempNumber == '1':
            tempBar.append('00011')
        elif tempNumber == '3':
            tempBar.append('00110')
        elif tempNumber == '5':
            tempBar.append('01010')
        elif tempNumber == '6':
            tempBar.append('01100')
        elif tempNumber == '8':
            tempBar.append('10010')
        elif tempNumber == '9':
            tempBar.append('10100')
    tempBar.append('000111')
    tempBar.insert(0,'1')
    newBar="".join(tempBar)
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
