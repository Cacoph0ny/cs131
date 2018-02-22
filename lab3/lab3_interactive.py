##
# Tharin Dresher-Hurst
# lab3_interactive.py
# 21 - 02 - 2018
# Created input loop
##

def main():
    userNumbList=[]
    userNumber=0
    while userNumber != -1:
        userNumber=int(input("Enter a postive number (put -1 to exit):\t"))
        userNumbList.append(userNumber)
    userNumbSort=sorted(userNumbList)
    userNumbSecondBig=userNumbSort[-2]
    print("The second biggest number is %d" %(userNumbSecondBig))

main()
