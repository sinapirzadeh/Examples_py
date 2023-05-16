import random 
import string

asbd = string.ascii_letters
symbols = '!@#$%^&*()_-+='
numbers = '0123456789'

all = asbd + symbols + numbers

while True:
    print('Choose an Option:\n\t1)create a Password\n\t2)Exit')
    choose = input('Your Choose : ')
    if choose == '1':
        length = int(input("Enter the Lenght of Password : "))
        password = ''.join(random.sample(all, length))
        print(password)
    elif choose == '2':
        break
    else:
        print('your choose is wrong!')
