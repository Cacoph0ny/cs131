##
# Tharin Dresher-Hurst
# lab7.py
# 18 - 04 - 18
# Started program - TDH
##

def mergeSorted(a, b):
    newList = []
    newList = a + b
    newList.sort()
    return newList

def main():
    a = [int(x) for x in input("Input numbers with a space between each: ").split()]
    b = [int(x) for x in input("Input numbers with a space between each: ").split()]
    a.sort()
    b.sort()
    trueList = mergeSorted(a, b)
    print('With lists a:',a,'and b:',b,"\nYou would get:",trueList)

main()
