#19- A teacher wants to draw one of his four students to erase the board. Make a program that helps him, reading the
# name of the students and writing the name of the chosen one on the screen.
import random
name_one = str(input('First students name:'))
name_two = str(input('Second students name:'))
name_three = str(input('Third students name:'))
name_four = str(input('Fourth students name:'))
list = [name_one, name_two, name_three, name_four]
chosen = random.choice(list)
print(f'The student chosen to erase the board is {chosen}.')
