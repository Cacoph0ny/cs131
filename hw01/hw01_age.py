##
# Tharin Dresher-Hurst
# hw01_age.py
# 2018 - 02 - 14
# Created the if elif chain
# 2018 - 02 - 15
# Fixed minor issues
##

def ageClass(x):
    if x <= 1:
        print("You are an infant.")
    elif x > 1 and x < 13:
        print("You are a child.")
    elif x >= 13 and x < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")

def main():
    userAgeInput=int(input("Enter your age in years:\t"))
    ageClass(userAgeInput)

main()
