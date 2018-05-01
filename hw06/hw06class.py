import pickle

class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed

class Information:
    def __init__(self, name, address, age, phoneNumber):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phoneNumber = phoneNumber
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phoneNumber(self):
        return self.__phoneNumber
    def __str__(self):
        return "Name: " + self.__name + "\nAddress: " + self.__address + "\nAge: " + self.__age + "\nPhone Number:" + self.__phoneNumber

def load_info(fileName):
    try:
        inputFile = open(fileName, 'rb')
        infoFile = pickle.load(inputFile)
        inputFile.close()
    except IOError:
        infoFile = {}

    return infoFile

def menu1():
    print('Main Menu')
    print('1 - Friends')
    print('2 - Family')
    print('3 - Personal')
    userInput = int(input('Enter selection: '))
    return userInput

def menu2():
    print('Info Menu')
    print('1 - Look up')
    print('2 - Add')
    print('3 - Change')
    print('4 - Delete')
    print('5 - Quit')
    userInput = int(input('Enter selection: '))
    return userInput

def lookUp(info):
    name = str(input("Enter name: "))
    print(info.get(name, 'Name not found'))

def add(info):
    name = str(input('Enter name: '))
    address = str(input('Enter address: '))
    age = str(input('Enter age: '))
    phoneNumber = str(input('Enter phone number: '))
    addInfo = Information(name, address, age, phoneNumber)
    if name not in info:
        print('Info added')
    else:
        print('Info already existed')

def change(info):
    name = str(input('Enter name: '))
    if name in info:
        address = str(input('Enter new address: '))
        age = str(input('Enter new age: '))
        phoneNumber = str(input('Enter new phone number: '))
        changeInfo = Information(name, address, age, phoneNumber)
        info[name] = changeInfo
        print('Info updated')
    else:
        print('Name not found')

def delete(info):
    name = str(input("Enter name: "))
    if name in info:
        del info[name]
        print('Info deleted')
    else:
        print('Name not found')

def saveFile(info, file):
    dataFile = open(file, 'wb')
    pickle.dump(info, dataFile)
    dataFile.close()
