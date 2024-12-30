#37-Write a Python program that reads any integer and asks the user to choose the conversion base: 1 for binary, 2 for
# octal, and 3 for hexadecimal
number = int(input('Enter an integer:'))
print('''Choose one of the bases for conversion:
[ 1 ] convert to  BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL''')
option = int(input('your choose:'))

match option:
    case 1:
        print(f'{number} converted to binary it becomes {bin(number)[2:]}.')
    case 2:
        print(f'{number} converted to octal it becomes {oct(number)[2:]}.')
    case 3:
        print(f'{number} converted to hexadecimal it becomes {hex(number)[2:]}.')
    case _:
        print('Invalid option try again!')
