##
# Tharin Dresher-Hurst
# hw05main.py main/actual program
# 25 - 04 - 18
# started functions - tdh
##

import hw05

def main():
    userScore, questions = hw05.quiz()
    grade = float(hw05.userScore(userScore, questions))
    print('You got %.2f%% correct.' %(grade))

main()
