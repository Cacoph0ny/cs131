##
# Tharin Dresher-Hurst
# hw06car.py
# 01 - 05 - 18
# created main - tdh
##

import hw06class

def main():
    myYear = int(input("Enter year: "))
    myMake = str(input("Enter make: "))
    my_car = hw06class.Car(myYear, myMake, 0)
    for ii in range(5):
        my_car.accelerate()
        print("Current speed ",my_car.get_speed())
    for ii in range(5):
        my_car.brake()
        print("Current speed ",my_car.get_speed())

main()
