data={
    '1020':{'balance':1000,'pin':1234,'history':[]},
    '1500':{'balance':2000,'pin':1254,'history':[]},
    '1602':{'balance':5000,'pin':1264,'history':[]},
    '1026':{'balance':8000,'pin':1274,'history':[]},}
acc_num=None
login_status=False
def welcome():
    print("Welcome to the ATM System")
    print("Please select an option:")
def show_menu():
    print("1. Login")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    
def login(acc,pin):
    if acc in data:
        if data[acc]['pin'] == pin:
            global acc_num
            global login_status
            acc_num=acc
            login_status = True
            print("Login successful")
        else:
            print("incorrect pin")
    else:
        print("acccount not found")        
def check_balance():
    if login_status and acc_num:
        print(f"Your balance is: {data[acc_num]['balance']}")   
    else:
        print("please again")    
def deposit(amount):
    if login_status and acc_num:
        if amount > 0:
            data[acc_num]['balance'] += amount
            data[acc_num]['history'].append(f"Deposited: {amount}")
            print(f"Deposited {amount}. New balance: {data[acc_num]['balance']}")
        else:
            print("Invalid deposit amount")
    else:
        print("please again")
def withdraw(amount):
    if login_status and acc_num:
        if amount > 0 and amount <= data[acc_num]['balance']:
            data[acc_num]['balance'] -= amount
            data[acc_num]['history'].append(f"Withdraw: {amount}")
            print(f"Withdraw {amount}. New balance: {data[acc_num]['balance']}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
    else:
        print("please again")


        

from datetime import date
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
'''0-mon
1-tue
2-wed
3-thu
4-fri
5-sat
6-sun'''
from datetime import datetime
now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.second)
print(now.strftime("%y/%m/%d"))#25/07/30
print(now.strftime("%y/%b/%d"))#25/Jul/30
print(now.strftime("%Y/%b/%d"))#2025/Jul/30
print(now.strftime("%B/%d/%y"))#July/30/25
print(now.strftime("%H:%M:%S %a"))#10:22:14 Wed
print(now.strftime("%H:%M:%S %A"))#10:22:14 Wednesday
print(now.strftime("%I:%M:%S %A %p"))#10:23:23 Wednesday AM
print(now.strftime("%A,%B %d,%y|%H:%M:%S %p"))#Wednesday,July 30,25|10:25:11 AM

from datetime import timedelta
nextweek=today+timedelta(4)#2025-08-03
nextweek=today-timedelta(4)#2025-07-26
after30min=now+timedelta(minutes=30)#2025-07-31 09:50:07.987456
print(after30min)
print(nextweek)

import sys
print(sys.argv)#['C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\python.exe', 'C:\\Users\\User\\Desktop\\classwork\\python course work\\19.Module.py']
print(sys.version)#3.10.12 (tags/v3.10.12:2023-07-03, 16:04:01) [MSC v.1934 64 bit (AMD64)]
print(sys.platform)#win32
print(sys.path)#['C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', '
print(sys.executable)#C:\Users\User\AppData\Local\Programs\Python\Python310\python.exe
print(sys.getdefaultencoding())#utf-8
# sys.exit() will terminate the program, so the following lines won't execute
print("This line will not be printed because sys.exit() was called.")
print("This line will not be printed because sys.exit() was called.")


import math
print(math.pi)#3.141592653589793
print(math.e)#2.718281828459045
print(math.sqrt(16))#4.0
print(math.pow(2, 3))#8.0
print(math.factorial(5))#120
print(math.gcd(12, 15))#3
print(math.sin(math.pi/2))#1.0
print(math.cos(math.pi))#-1.0
print(math.tan(math.pi/4))#1.0
print(math.log(100, 10))#2.0
print(math.log2(8))#3.0
print(math.log10(1000))#3.0
print(math.ceil(4.2))#5
print(math.floor(4.8))#4
print(math.trunc(4.8))#4
print(math.isqrt(16))#4
print(math.degrees(math.pi))#180.0

import random
print(random.randint(1, 10))#Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))#Random choice from the list
print(random.choices(['apple', 'banana', 'cherry'], k=2))#Random choice with replacement
print(random.sample([1, 2, 3, 4, 5], 3))#Random sample of 3 elements from the list
print(random.uniform(1.0, 10.0))#Random float between 1
print(random.random())#Random float between 0.0 and 1.0
print(random.shuffle([1, 2, 3, 4, 5]))#Shuffles the list in place
print(random.seed(42))#Sets the seed for reproducibility

import collections
print(collections.Counter(['apple', 'banana', 'apple', 'orange']))#Counter({'apple': 2, 'banana': 1, 'orange': 1})
print(collections.defaultdict(int))#defaultdict(<class 'int'>, {})

##game
import random
shivani_score=0
nani_score=0
while shivani_score<100 and nani_score<100:
    shivani=input("Shivani, press Enter to roll the dice...")
    nani=input("Nani, press Enter to roll the dice...")
    shivani_roll=random.randint(1, 6)
    nani_roll=random.randint(1, 6)
    print(f"Shivani rolled: {shivani_roll}, Nani rolled: {nani_roll}")
    
    if shivani_roll > nani_roll:
        shivani_score += 10
        print("Shivani wins this round!")
    elif nani_roll > shivani_roll:
        nani_score += 10
        print("Nani wins this round!")
    else:
        print("It's a tie!")
    
    print(f"Current scores - Shivani: {shivani_score}, Nani: {nani_score}")




























