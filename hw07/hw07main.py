##
# Tharin Dresher-Hurst
# hw07main.py
# 09 - 05 - 18
# started and finished - tdh
##

import hw07class

def main():
    eName = str(input('Enter employee name: '))
    eNumber = str(input('Enter employee number: '))
    eShift = str(input('Enter employee shift (1 for day, 2 for night): '))
    supWork = str(input("Is the employee a supervisor(1) or worker(2): "))
    if supWork == '2':
        ePayRate = str(input('Enter employee pay rate: '))
        worker = hw07class.ProductionWorker(eName, eNumber, eShift, ePayRate)
        print('Name:\t%s' %(worker.get_name()))
        print('ID:\t%s' %(worker.get_number()))
        print('Shift:\t%s' %(worker.get_shift()))
        print('Pay:\t%s/hr' %(worker.get_payRate()))
    else:
        eSalary = str(input('Enter employee salary: '))
        eBonus = str(input('Enter employee bonus: '))
        supervisor = hw07class.ShiftSupervisor(eName, eNumber, eShift, eSalary, eBonus)
        print('Name:\t%s' %(supervisor.get_name()))
        print('ID:\t%s' %(supervisor.get_number()))
        print('Shift:\t%s' %(supervisor.get_shift()))
        print('Salary:\t%s' %(supervisor.get_salary()))
        print('Bonus:\t%s' %(supervisor.get_bonus()))

main()
