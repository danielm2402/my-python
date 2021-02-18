# Find the largest number

number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
number3 = int(input('Number 3: '))

bNumber = number1
if number2 > bNumber:
    bNumber = number2
if number3 > bNumber:
    bNumber = number3

print('The largest number is:', bNumber)
