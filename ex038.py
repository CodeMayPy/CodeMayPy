#38- Write a program that reads two integers and compares them, displaying a message on the screen:
# – The first value is greater
# – The second value is greater
# – There is no greater value, both are equal
first_number = int(input('Enter an integer:'))
second_number = int(input('Enter other integer:'))
if first_number > second_number:
    print(f'The number {first_number} is greater than {second_number}.')
elif first_number < second_number:
    print(f'The number {second_number} is greater than {first_number}.')
else:
    print('The two numbers are the same!')
