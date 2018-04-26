##
# Tharin Dresher-Hurst
# hw04Functions.py
# 09 - 04 - 18
# Started - TDH
##

def telephoneName(phoneNum):
    dataFile = open('data1.txt','r')
    dataLine = dataFile.readline()
    while True:
        if phoneNum == '':
            print('Number not found')
        elif phoneNum in dataLine:
            nameIs, sep, tail = dataLine.partition(', ')
            print('Name is: %s' %(nameIs))
            break
        elif dataLine == '':
            print('Name is not found')
            return
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return nameIs

def nameSocial(name):
    dataFile = open('data2.txt','r')
    dataLine = dataFile.readline()
    while True:
        if name == '':
            print('SSN not found')
        elif name in dataLine:
            nameIs, sep, tail  = dataLine.partition(', ')
            print('SSN is: %s' %(tail))
            return tail
        elif dataLine == '':
            print('SSN not found')
            return
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return tail

def socialIncome(ssn):
    dataFile = open('data3.txt','r')
    dataLine = dataFile.readline()
    while True:
        if ssn == '':
            print('Income not found')
            return
        elif ssn in dataLine:
            nameIs, sep, tail  = dataLine.partition(', ')
            print('SSN is: %s' %(tail))
            break
        elif dataLine == '':
            print('Income not found')
            return
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return tail
