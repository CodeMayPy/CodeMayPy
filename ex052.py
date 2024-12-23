#52- Write a program that reads an integer and tells whether or not it is a prime number.
number = int(input('Enter a integer number:'))
tot = 0
for c in range(1, number, +1):
    if number % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m The number {number} was divisible {tot} times.')
if tot == 2:
    print('And that is why he is a prime number.')
else:
    print('And that is why it is not a prime number.')