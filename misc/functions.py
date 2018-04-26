import random

def writeName():
    playerName = open('player.txt','w')
    nameTemp = str(input("Enter character name\n"))
    playerName.write(nameTemp)
    return

def readName():
    playerName = open('player.txt','r')
    nameTemp = playerName.readline()
    return nameTemp

def movementExplore():
    userMove = str(input('Move forward?(yes/no)\n'))
    while userMove == 'yes':
        print('You move to the next room')
        whatHappened = event()
        if whatHappened == 0:
            userReward = reward()
            print('Your get %s' %(userReward))
            userMove = str(input('Move forward?(yes/no)\n'))
        elif whatHappened == 1:
            fightReward = userFight()
            userMove = str(input('Move forward?(yes/no)\n'))
        else:
            userMove = str(input('Move forward?(yes/no)\n'))
    return

def event():
    rng = random.randint(1,100)
    if rng >= 80:
        print('You found loot.')
        return 0
    elif rng >= 30 and rng < 80:
        print('The room has a monster!')
        return 1
    else:
        print('The room is empty.')
        return 2

def reward():
    rng = random.ranint(1,3)
    if rng == 3:
        print('Large pile of coins!')
        rewardCoins = random.randint(15,25)
        return str('%d coins' %(rewardCoins))

def userFight():
    reward = reward()
    print("You beat the monster!\nYou got %s" %(reward))

def actions():
    userAction = str(input('What do you want to do?\n(explore, inv, level, help)'))
    return userAction

def userHelp():
    print('Type "explore" to start moving forward\nType "inv" to view and manage inventory(Does nothing at them moment)\nType "level" to level up or view stats (does nothing at the moment)\nType "exit" to save and exit')

def saveFile():
    # write a bunch of shit to save
    return
