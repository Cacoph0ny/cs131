##
# Tharin Dresher-Hurst
# hw01_age.py
# 2018 - 02 - 14
# Created the if elif chain
##

def bmiCalc(height, weight):
    bmiResult=weight*703/(height**2)
    return bmiResult

def main():
    userWeight=float(input("Enter weight in pounds:\t"))
    userHeight=float(input("Enter height in inches:\t"))
    userBmi=bmiCalc(userHeight,userWeight)
    if userBmi < 18.5:
        print("You are under weight with a BMI of %.1f." %(userBmi))
    elif userBmi <= 25 and userBmi >= 18.5:
        print("You are normal weight with a BMI of %.1f." %(userBmi))
    else:
        print("You are over weight with a BMI of %.1f." %(userBmi))

main()
