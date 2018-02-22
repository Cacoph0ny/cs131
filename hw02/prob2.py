##
# Tharin Dresher-Hurst
# hw01_age.py
# 2018 - 02 - 14
# Created the if elif chain
##

def main():
    userInputTime=int(input("Input amount of seconds:\t"))
    timeDays=userInputTime//86400
    timeHours=(userInputTime-(timeDays*86400))//3600
    timeMinutes=(userInputTime-(timeDays*86400)-(timeHours*3600))//60
    timeSeconds=userInputTime-(timeDays*86400)-(timeHours*3600)-(timeMinutes*60)
    print("%d seconds would be %d day(s), %d hour(s), %d minute(s) and %d second(s)" %(userInputTime, timeDays, timeHours, timeMinutes, timeSeconds))

main()
