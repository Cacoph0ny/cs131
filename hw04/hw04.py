##
# Tharin Dresher-Hurst
# hw04.py
# 09 - 04 - 18
# Started - TDH
##

import hw04Functions

def main():
    phoneNum = str(input('Input phone number: '))
    name = hw04Functions.telephoneName(phoneNum)
    ssn = hw04Functions.nameSocial(name)
    income = hw04Functions.socialIncome(ssn)

main()
