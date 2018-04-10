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
            nameIs = dataLine.strip(',')
            print(nameIs)
            break
        else:
            dataLine = dataFile.readline()
    dataFile.close()
    return dataLine

def nameSocial(name):
#    dataFile = open('data2.txt','r')
#    dataLine = dataFile.readline()
#    #while True:
#        if name in dataLine:
#            print(type(dataLine))
#    if dataLine == '':
#        print('That name is not in the list.')
#    else:
#        print('SSN is: %s' %(dataLine))
#    dataFile.close()
    return 2

def socialIncome(ssn):
    dataFile = open('data3.txt','r')
    dataLine = dataFile.readline()
    while dataLine != '' and dataLine != ssn:
        dataLine = dataFile.readline()
    if dataLine == '':
        print('SSN not found in list.')
    else:
        print('Income is: %s' %(dataLine))
    dataFile.close()
    return dataLine
