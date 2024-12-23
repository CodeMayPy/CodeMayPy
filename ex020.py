#20- The same teacher from challenge 19 wants to draw the order in which the students' work will be presented. Make a program that
# read the names of the four students and show the order drawn.
import random
first_name = str(input('First students name:'.strip()))
second_name = str(input('Second students name:'.strip()))
third_name = str(input('Third students name:'.strip()))
fourth_name = str(input('Fourth students name:'.strip()))
list = [first_name, second_name, third_name, fourth_name]
random.shuffle(list)
print('The order of presentation of students will be:')
print(list)
