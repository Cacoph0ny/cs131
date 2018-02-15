##
# Tharin Dresher-Hurst
# hw01_age.py
# 2018 - 02 - 14
# Created the if elif chain
##

def main():
    packageWeight=float(input("Package weight in pound:\t"))
    if packageWeight <= 2:
        packagePrice=packageWeight*1.5
        print("It would be %.2f to ship that package" %(packagePrice))
    elif packageWeight > 2 and packageWeight <= 6:
        packagePrice=packageWeight*3
        print("It would be %.2f to ship that package" %(packagePrice))
    elif packageWeight > 6 and packageWeight <=10:
        packagePrice=packageWeight*4
        print("It would be %.2f to ship that package" %(packagePrice))
    else:
        packagePrice=packageWeight*4.75
        print("It would be %.2f to ship that package" %(packagePrice))

main()
