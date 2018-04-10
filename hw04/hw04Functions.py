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
        if phoneNum in dataLine:
            nameIs, sep, tail = dataLine.partition(', ')
            print('Name is: %s' %(nameIs))
            break
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return nameIs

def nameSocial(name):
    dataFile = open('data2.txt','r')
    dataLine = dataFile.readline()
    while True:
        if name in dataLine:
            nameIs, sep, tail  = dataLine.partition(', ')
            print('SSN is: %s' %(tail))
            break
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return tail

def socialIncome(ssn):
    dataFile = open('data3.txt','r')
    dataLine = dataFile.readline()
    while True:
        if ssn in dataLine:
            nameIs, sep, tail = dataLine.partion(', ')
            print('Name is: %s' %(tail))
            break
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return tail
