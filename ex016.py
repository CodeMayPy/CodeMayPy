# Create a program that reads any real number from the keyboard and displays its entire portion on the screen.
import math
number = float(input('Enter a value:'))
print('The value typed was {} and its entire part is {}.'.format(number, math.trunc(number)))
