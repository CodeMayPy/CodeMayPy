# Write a program that reads any number and displays its factorial.
# just in four lines
'''from math import factorial
number = int(input('Enter a number:'))
result = factorial(number)
print(f'The factorial of {number}! is {result}')'''

# or you can make it prettier
number = int(input('Enter a number:'))
counter = number
fat = 1
print(f'Calculating {number}! =', end= ' ')
while counter > 0:
    print(f'{counter}', end= ' ' )
    print(' x ' if counter > 1 else ' = ', end=' ')
    fat *= counter
    counter -= 1
print(f'{fat}.')
