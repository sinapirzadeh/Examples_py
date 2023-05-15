import calendar
import random
import time

# show result by {Format}
num_1 = 2
num_2 = 4
sum = num_1 + num_2
print("sum is {0} operation is {1} + {2}".format(sum, num_1, num_2))

print('=====================================')

# Number is Odd or Even
num_3 = int(input('Enter a Number : '))
result_1 = 'Odd' if (num_3 % 2) == 0 else 'Even'
print(result_1)

print('=====================================')

# Number is Positive or Negative
num_4 = int(input('Enter a Number : '))
result_2 = 'Positive' if num_4 > 0 else 'Negative'
print(result_2)

print('=====================================')

# Sum of Total
total = [1, 4, 5, 6, 8, 9, 11, 55]

for i in total:
    sum = sum + i
    print(sum)

print('=====================================')

# Sum of Total too ensor
total_2 = [(1, 2), (4, 5), (5, 6), (6, 8)]
for i, b in total_2:
    print(i + b)

print('=====================================')

# Sum of Total too ensor
total_3 = {'name': 'sian', 'job': 'Developer', 'age': '18'}
for x, y in total_3.items():
    print(x,y)

print('=====================================')

# parameter of {Range}
for i in range(30, 0, 2):
    print(12)

print('=====================================')

# a move to b and b move to a
a = 12
b = 24
a, b = b, a
print(f'a, b=> {a, b}')

print('=====================================')

# Find the square root
num_5 = 9
num_sqrt = num_5 ** 0.5
print(num_sqrt)

print('=====================================')

# Create Random Number
print(random.randint(0, 9))

print('=====================================')

# Factorial Number
num_6 = 5
factorial = 1
if num_6 < 0:
    print('Does not exist')
elif num_6 == 0:
    print('factorial')
else:
    for i in range(1, num_6 + 1):
        factorial = factorial * i

print(factorial)

print('=====================================')

# string Length
s = 'Sina Pirzadeh'
print(len(s))

print('=====================================')

# Find ASCII
cher = 'A'
print('ASCII Value : ', ord(cher))

print('=====================================')

# Reverse a string
s = 'sina pirzadeh'
print(s[::-1])

print('=====================================')

# Show  Calender
yy = 2023  # year
mm = 2  # month - Feb
print(calendar.month(yy, mm))

print('=====================================')

# All Multiple a Number
num_7 = int(input('Enter a Number for Multiple : '))
for i in range(1, 10 + 1):
    print(num_7, 'X', i, ' = ', num_7 * i)

print('=====================================')

# number of bin, oct, hex
doc = 5
print((bin(doc), 'in binary'))
print((oct(doc), 'in octal'))
print((hex(doc), 'in hexadecimal'))

print('=====================================')

# natural numbers
sum_1 = 0
num_8 = 7

if num_8 < 0:
    print('Negative')
else:
    while num_8 > 0:
        sum_1 += num_8
        num_8 -= 1

print('Sum :', sum_1)


print('=====================================')

# check the first number
num_9 = 7

if num_9 > 1:
    for i in range(2, num_9):
        if (num_9 % i) == 0:
            print('Not Prime')
            break
        else:
            print('Prime')
else:
    print('Not Prime')


print('=====================================')

# Create a time Delay
print('Task A')
time.sleep(2)  # 2 seconds
print('Task B')

print('=====================================')

# Quiz
if 0 ** 0 == 1:
    print(not True)
else:
    print(not False)

    
print('=====================================')

# Starz i think
rows = 5
b = 0

for i in range(rows, 0, -1):
   b+=1
   for j in range(1,i+1):
       print(b, end = " ")
   print("\r")

row = 6
num = row

for i in range(row, 0,-1):
   for j in range(0, i):
       print(num, end = " ")
   print("\r")

rows = 5
for i in range(rows, 0,-1):
    num = i
    for j in range(0, i):
        print(num, end = " ")
    print("\r")


print('=====================================')
