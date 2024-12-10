# Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.
number = int(input('Informe um número:'))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10
print(f'Analyzing your number: {number}.')
print(f'Your unit is {unit}.')
print(f'Your ten is {ten}.')
print(f'Your hundred is {hundred}.')
print(f'Your thousand is {thousand}.')
