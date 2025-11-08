from random import randint
from time import sleep
import math
# might be more.

Balance = 0
Jobs = []
Name = 'John Doe'
Gender = 'Unknown'
Money_Symbol = '$'
Banked = 0
Commands = ['end','deposit','withdraw']

def start():
    global Balance, Gender, Name, Jobs
    print('Starting Bank Game (Version 0 [Open Alpha])')
    Name = input("Please select a Character Name: ")
    Gender_Input = int(input('Please select a gender!\n[1 = Male, 2 = Female] '))
    if Gender_Input == 2:
        Gender = 'Female'
    else:
        Gender = 'Male'
    Balance = randint(200, 325)
    if Name == 'admin':
        Balance = math.inf
    print("Creating Character...")
    sleep(2)
    print(f"Character Created! \nName: {Name}\nGender: {Gender}\nBalance: {Money_Symbol}{Balance}")
    sleep(4)
    SelectCommand()


def deposit():
    global Balance, Banked, Jobs
    print(f"Your Balance: {Money_Symbol}{Balance}")
    DepAmount = int(input(f'How much {Money_Symbol} do you want to deposit?\n {Money_Symbol}'))
    if DepAmount > Balance:
        print('You do not have sufficient funds to deposit this amount.')
    else:
        print("Processing Deposit...")
        sleep(2)
        Balance -= DepAmount
        Banked += DepAmount
        print(f"You have stored {Money_Symbol}{DepAmount} in the bank!\nYour new balance is: {Money_Symbol}{Balance}\nCurrent bank balance: {Money_Symbol}{Banked}")
        sleep(1)
        SelectCommand()

def withdraw():
    global Balance, Banked, Jobs
    print(f"Your Bank Balance: {Money_Symbol}{Banked}")
    WithAmount = int(input(f'How much {Money_Symbol} do you want to withdraw?\n {Money_Symbol}'))
    if WithAmount > Banked:
        print('You do not have sufficient bank funds to withdraw this amount.')
    else:
        print("Processing Withdrawal...")
        sleep(2)
        Banked -= WithAmount
        Balance += WithAmount
        print(f"You have withdrew {Money_Symbol}{WithAmount} from the bank!\nYour new balance is: {Money_Symbol}{Balance}\nNew bank balance: {Money_Symbol}{Banked}")
        SelectCommand()

def SelectCommand():
    global Balance, Banked, Name, Jobs

    commandInput = input(f'Please type a command into the input box.\n COMMANDS: {Commands} ')

    if Name != 'John Doe':
        if commandInput:
         if commandInput == 'end':
            print(f'Ending game, thank you for playing!')
            sleep(0.8)
            print(f'STATS:\nBalance: {Money_Symbol}{Balance}\nBank: {Money_Symbol}{Banked}\nName: {Name}\nGender: {Gender}\nJobs: {Jobs}')
            exit()
         elif commandInput == 'deposit':
            deposit()
         elif commandInput == 'withdraw':
            withdraw()
    

if __name__ == '__main__':
   # SelectCommand()
     start()
