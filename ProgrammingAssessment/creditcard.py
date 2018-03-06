##
# Tharin Dresher-Hurst
#
# 05 - 03 - 18
# Did everything - TDH
##

def main():
    creditLimit=float(input("Enter the credit limit: "))
    creditBalance=float(input("Enter the card balance: "))
    creditApr=float(input("Enter APR: "))
    creditMonth=float(input("Enter monthly payment: "))
    counter = 0
    paymentTotal = 0
    while creditBalance != 0:
        if counter == 0:
            print("Month\t","Balance\t","Interest\t","Payment\t","New Balance")
            counter += 1
        elif counter == 1:
            interest= creditBalance * (creditApr/100) / 12
            newBalance= creditBalance + interest - creditMonth
            print("%d\t %7.2f\t %7.2f\t %7.2f\t %7.2f" %(counter, creditBalance, interest, creditMonth, newBalance))
            creditBalance=newBalance
            paymentTotal= paymentTotal + creditMonth
            counter += 1
        else:
            if creditBalance < creditMonth:
                interest= creditBalance * (creditApr/100) / 12
                creditMonth= creditBalance + interest
                newBalance= creditBalance + interest - creditMonth
                print("%d\t %7.2f\t %7.2f\t %7.2f\t %7.2f" %(counter, creditBalance, interest, creditMonth, newBalance))
                creditBalance=newBalance
                paymentTotal= paymentTotal + creditMonth
            else:
                interest= creditBalance * (creditApr/100) / 12
                newBalance= creditBalance + interest - creditMonth
                print("%d\t %7.2f\t %7.2f\t %7.2f\t %7.2f" %(counter, creditBalance, interest, creditMonth, newBalance))
                creditBalance=newBalance
                counter += 1
                paymentTotal= paymentTotal + creditMonth
    print("It will take $%.2f over %d month(s) to pay off this debt." %(paymentTotal, counter))

main()
