##
# Tharin Dresher-Hurst
# hw06Info.py
# 01 - 05 - 18
# created main - tdh
##

import hw06class
import pickle

FRIENDS = 1
FAMILY = 2
PERSONAL = 3
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAMEFR = 'infoFileFriends.dat'
FILENAMEFA = 'infoFileFamily.dat'
FILENAMEPE = 'infoFilePersonal.dat'

def main():
    choice = hw06class.menu1()
    if choice == FRIENDS:
        my_contacts = hw06class.load_info(FILENAMEFR)
        while choice != QUIT:
            choice = hw06class.menu2()
            if choice == LOOKUP:
                hw06class.lookUp(my_contacts)
            elif choice == ADD:
                hw06class.add(my_contacts)
            elif choice == CHANGE:
                hw06class.change(my_contacts)
            elif choice == DELETE:
                hw06class.delete(my_contacts)
        hw06class.saveFile(my_contacts,FILENAMEFR)
    elif choice == FAMILY:
        my_contacts = hw0hw06class.load_info(FILENAMEFA)
        while choice != QUIT:
            choice = hw06class.menu2()
            if choice == LOOKUP:
                hw06class.lookUp(my_contacts)
            elif choice == ADD:
                hw06class.add(my_contacts)
            elif choice == CHANGE:
                hw06class.change(my_contacts)
            elif choice == DELETE:
                hw06class.delete(my_contacts)
        hw06class.saveFile(my_contacts,FILENAMEFA)
    elif choice == PERSONAL:
        my_contacts = hw0hw06class.load_info(FILENAMEPE)
        while choice != QUIT:
            choice = hw06class.menu2()
            if choice == LOOKUP:
                hw06class.lookUp(my_contacts)
            elif choice == ADD:
                hw06class.add(my_contacts)
            elif choice == CHANGE:
                hw06class.change(my_contacts)
            elif choice == DELETE:
                hw06class.delete(my_contacts)
        hw06class.saveFile(my_contacts,FILENAMEPE)
    else:
        print('Error')

main()
