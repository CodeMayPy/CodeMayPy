# Make a program that calculates the sum of all numbers that are multiples of three and that are in the
# range from 1 to 500.
soma = 0
counter = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        counter = counter + 1
        soma = soma + c
print(f'The sum of all {counter} requested values is {soma}.')
