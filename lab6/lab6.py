##
# Tharin Dresher-Hurst
# lab6.py
# 21 - 03 - 2018
# Started Program - TDH
##

import random

startScore = 0

def blackJackHeader():
    print('*'*25, '\n**  CS 131 Blackjack  **')
    print('*'*25)
    if str(input('Do you want to play? (y/n) ')) == 'n':
        exit()

def blackJackStart():
    firstCard=drawCard()
    playerScore=startScore
    print("\nYou got\t\t\t%d\nYour Score\t\t%d" %(firstCard, playerScore))
    return playerScore + firstCard

def drawCard():
    card=random.randint(1,11)
    if card == 11:
        if str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'high':
            card = 10
            return card
        elif str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'low':
            card = 1
            return card
        else:
            print('Invalid Input Exiting')
            exit()
    return card

def drawCardDealer():
    card=random.randint(1,11)
    return card

def playerTurn(currentScore):
    while currentScore <= 21 and currentScore != -1:
        turnScore = currentScore
        turnCard = drawCard()
        if (turnScore+turnCard) > 21:
            print('You drew %d\nYou went over 21 and lose.' %(turnCard))
            currentScore = -1
            return currentScore
        else:
            turnScore += turnCard
            print('You got\t\t\t%d\nYour Score\t\t%d' %(turnCard, turnScore))
            currentScore = turnScore
        if str(input("Draw again? (y/n) ")) == 'n':
            return currentScore
    return currentScore

def dealerTurn(dealerScore):
    while dealerScore < 17 and dealerScore != -1:
        dealCard = drawCardDealer()
        if dealCard == 11:
            if (dealerScore+11) > 22:
                dealCard = 1
            else:
                dealCard = 10
        if (dealerScore + dealCard) > 21:
            dealerScore += dealCard
            print('Dealer got\t\t%d\nDealer Score\t\t%d\nDealer busted' %(dealCard, dealerScore))
            dealerScore = -1
        elif (dealerScore + dealCard) > 17:
            dealerScore += dealCard
            print('Dealer got\t\t%d\nDealer Score\t\t%d\nDealer Holds' %(dealCard, dealerScore))
            return dealerScore
        else:
            dealerScore += dealCard
            print('Dealer got\t\t%d\nDealer Score\t\t%d' %(dealCard, dealerScore))
            if dealerScore == 17:
                print('Dealer Holds')
                return dealerScore
    return dealerScore

def whoWon(playerScore, dealerScore):
    if playerScore > dealerScore:
        print('You won with %d points!' %(playerScore))
    if dealerScore > playerScore:
        print('Dealer won with %d points!' %(dealerScore))
    elif playerScore == dealerScore:
        print('Tie with %d points!' %(playerScore))

def main():
    blackJackHeader()
    playerScore=blackJackStart()
    player=playerTurn(playerScore)
    if playerScore == -1:
        print('Dealer won!')
    else:
        dealerStart=0
        dealer=dealerTurn(dealerStart)
        whoWon(player, dealer)

main()
