##
# Tharin Dresher-Hurst
# hw07class.py
# 09 - 05 - 18
# started and finished - tdh
##

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, payRate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__payRate = payRate
    def get_shift(self):
        if self.__shift == '1':
            self.__shift = 'day'
        else:
            self.__shift = 'night'
        return self.__shift
    def get_payRate(self):
        return self.__payRate

class ShiftSupervisor(Employee):
    def __init__(self, name, number, shift, salary, bonus):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__salary = salary
        self.__bonus = bonus
    def get_shift(self):
        if self.__shift == '1':
            self.__shift = 'day'
        else:
            self.__shift = 'night'
        return self.__shift
    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus
