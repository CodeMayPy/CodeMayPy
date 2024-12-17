# Write a program that reads two integers and compares them, displaying a message on the screen:
# – The first value is greater
# – The second value is greater
# – There is no greater value, both are equal
first_number = int(input('Enter an integer:'))
second_number = int(input('Enter other integer:'))
if first_number > second_number:
    print(f'The number {first_number} is greater than {second_number}.')
elif n1 < n2:
    print('O número {} é maior que o {}.'.format(n2, n1))
else:
    print('Os dois números são iguais!')
