import random

startScore = 0

deckDict = {12:'2 of hearts',13:'3 of hearts',14:'4 of hearts',15:'5 of hearts',16:'6 of hearts',17:'7 of hearts',18:'8 of hearts',19:'9 of hearts',20:'10 of hearts',21:'jack of hearts',22:'queen of hearts',23:'king of hearts',24:'ace of hearts',32:'2 of diamonds',33:'3 of diamonds',34:'4 of diamonds',35:'5 of diamonds',36:'6 of diamonds',37:'7 of diamonds',38:'8 of diamonds',39:'9 of diamonds',20:'40 of diamonds',41:'jack of diamonds',42:'queen of diamonds',43:'king of diamonds',44:'ace of diamonds',52:'2 of spades',53:'3 of spades',54:'4 of spades',55:'5 of spades',56:'6 of spades',57:'7 of spades',58:'8 of spades',59:'9 of spades',60:'10 of spades',61:'jack of spades',62:'queen of spades',63:'king of spades',64:'ace of spades',72:'2 of clubs',73:'3 of clubs',74:'4 of clubs',75:'5 of clubs',76:'6 of clubs',77:'7 of clubs',78:'8 of clubs',79:'9 of clubs',80:'10 of clubs',81:'jack of clubs',82:'queen of clubs',83:'king of clubs',84:'ace of clubs'}

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
    tempDict = deckDict.copy()
    suit=random.randint(1,4)
    if suit == 1:
        cardValue = random.randint(12,24)
        cardString = tempDict.pop(cardValue)
        if cardValue <= 20:
            cardValue = cardValue - 10
            return cardValue, cardString
        elif cardValue > 20 and cardValue < 24:
            cardValue = 10
            return cardValue, cardString
        elif cardValue == 24:
            if str(input('You got an ACE! Do you want it high or low? ')) == 'high':
                cardValue = 10
                return cardValue, cardString
            elif str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'low':
                cardValue = 1
                return cardValue, cardString
    elif suit == 2:
        cardValue = random.randint(32,44)
        cardString = tempDict.pop(cardValue)
        if cardValue <= 40:
            cardValue = cardValue - 30
            return cardValue, cardString
        elif cardValue > 40 and cardValue < 44:
            cardValue = 10
            return cardValue, cardString
        elif cardValue == 44:
            if str(input('You got an ACE! Do you want it high or low? ')) == 'high':
                cardValue = 10
                return cardValue, cardString
            elif str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'low':
                cardValue = 1
                return cardValue, cardString
    elif suit == 3:
        cardValue = random.randint(52,64)
        cardString = tempDict.pop(cardValue)
        if cardValue <= 60:
            cardValue = cardValue - 50
            return cardValue, cardString
        elif cardValue > 60 and cardValue < 64:
            cardValue = 10
            return cardValue, cardString
        elif cardValue == 64:
            if str(input('You got an ACE! Do you want it high or low? ')) == 'high':
                cardValue = 10
                return cardValue, cardString
            elif str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'low':
                cardValue = 1
                return cardValue, cardString
    else:
        cardValue = random.randint(72,84)
        cardString = tempDict.pop(cardValue)
        if cardValue <= 80:
            cardValue = cardValue - 10
            return cardValue, cardString
        elif cardValue > 20 and cardValue < 84:
            cardValue = 10
            return cardValue, cardString
        elif cardValue == 84:
            if str(input('You got an ACE! Do you want it high or low? ')) == 'high':
                cardValue = 10
                return cardValue, cardString
            elif str(input('You got an ACE! Do you want it high(10) or low(1)? ')) == 'low':
                cardValue = 1
                return cardValue, cardString

def drawCardDealer():
    card=random.randint(1,11)
    return card

def playerTurn(currentScore):
    while currentScore <= 21 and currentScore != -1:
        turnScore = currentScore
        turnCard, turnString = drawCard()
        if (turnScore+turnCard) > 21:
            print('You drew %s\nYou went over 21 and lose.' %(turnString))
            currentScore = -1
            return currentScore
        else:
            turnScore += turnCard
            print('You got\t\t\t%s\nYour Score\t\t%d' %(turnString, turnScore))
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
