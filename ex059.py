#Create a program that reads two values and displays a menu on the screen:
#[ 1 ] add
#[ 2 ] multiply
#[ 3 ] bigger
#[ 4 ] new numbers
#[ 5 ] exit the program
#Your program must perform the requested operation in each case.

first_value = int(input('Enter a number:'))
second_value = int(input('Enter other number:'))
option = 0

while option != 5:
    print('''Choose an option...
         [1] Add
         [2] Multiply
         [3] Bigger
         [4] New numbers
         [5] Exit the program ''')
    choice = int(input('Enter your choice:'))
    if choice == 1:
       add = first_value + second_value
       print(f'The sum of {first_value} + {second_value} is {add}')
    elif choice == 2:
       multiply = first_value * second_value
       print(f'The product of {first_value} and {second_value} is {multiply}')
    elif choice == 3:
        if first_value > second_value:
            bigger = first_value
        else:
            bigger = second_value
        print(f'Between {first_value} and {second_value} the largest value is {bigger}.')
    elif choice == 4:
        print('Enter the numbers again:')
        first_value = int(input('Enter a number:'))
        second_value = int(input('Enter other number:'))
    elif choice == 5:
         print('Finishing...')
    else:
        print('Invalid option. Try again.')
print('End of program.')