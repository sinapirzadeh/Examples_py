import time
from os import system

while True:
    choose = input('Do you want to start? (y/n): ')
    if 'y' in choose.lower():
        hour = int(input('Enter hour : '))
        minutes = int(input('Enter minutes : '))
        second = int(input('Enter second : '))
        total = hour * 60 * 60 + minutes * 60 + second
        print('Timer start now ... ')
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            system('clear')
        print("timer is don!")
    elif 'n' in choose.lower():
        break
    else:
        print('is down !')
