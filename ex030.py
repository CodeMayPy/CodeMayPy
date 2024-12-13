# Create a program that reads an integer and tells you whether it is even or odd.
number = int(input('Enter a number:'))
result = number % 2
if result ==0:
    print(f'The number {number} its even.')
else:
    print(f'The number {number} its odd.')
