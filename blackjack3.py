##
#
# Blackjack.py
# Author Tharin Dresher-Hurst
# csA122
# Edits
# 4-10-17 TDH First Draft
# 4-16-17 TDH Work on Main function
# 4-17-17 TDH Better Names
# 4-18-17 TDH Finished gamePlayer and gameDealer
#
##

# Imports
import random

# Starting Variables
startCard=0

# Function for Calculations
def gameHeader():
    print("*"*25)
    print("**  cs A122 Blackjack  **")
    print("*"*25)
    if str(input("Do you want to play? (y/n) ")) =='n':
        exit()
    return

def gameStart():
    startCard=gameDraw()
    startScore=startCard
    print("\nYou got\t\t\t %d \nYour Score\t\t %d" %(startScore, startScore))
    if str(input("\nDraw second card? (y/n) "))=='n':
        exit()
    return startScore

def gameDraw():
    card=random.randint(1,11)
    if card==11:
        card=10
    return card

def gamePlayer(playerTemp):
    while playerTemp<=21 and playerTemp !=-1:
        gamePlayerScore=playerTemp
        gameCard=gameDraw()
        if (gamePlayerScore+gameCard)>21:
            print("You drew a %d \nYou went over 21 and lose." %gameCard)
            playerTemp=-1
        else:
            playerTemp=gamePlayerScore+gameCard
            print("\nYou got a\t\t %d \nYour Score\t\t %d" %(gameCard, playerTemp))
            if str(input("\nDo you want to continue? (y/n) ")) != "y":
                return playerTemp
    return playerTemp

def gameDealer(dealerTemp):
    while dealerTemp<17 and dealerTemp !=-1:
        dealerCard=gameDraw()
        if (dealerTemp+dealerCard)>21:
            dealerTemp=dealerTemp+dealerCard
            print("Dealer got %d \nDealer's Score is \t %d \nDealer busted." %(dealerCard, dealerTemp))
            dealerTemp=-1
        elif (dealerTemp+dealerCard)>17:
            dealerTemp=dealerTemp+dealerCard
            print("\nDealer got\t\t %d \nDealer's Score is \t %d" %(dealerCard, dealerTemp))
            print("\nDealer has %d points and holds." %dealerTemp)
            return dealerTemp
        else:
            dealerTemp=dealerTemp+dealerCard
            print("\nDealer got\t\t %d \nDealer's Score is \t %d" %(dealerCard, dealerTemp))
    return dealerTemp

def gameWin(playerS, dealerS):
    if playerS>dealerS:
        print("\nYou win! With %d points" %playerS)
    elif dealerS>playerS:
        print("\nDealer Wins! With %d points" %dealerS)
    else:
        print("\nYou tie! With %d points" %playerS)

# Main Function
def main():
    gameEnd=gameHeader()
    playerScore=gameStart()
    test1=gamePlayer(playerScore)
    dealScore=0
    test2=gameDealer(dealScore)
    gameWin(test1, test2)

main()
