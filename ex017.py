# Write a program that reads the length of the opposite and adjacent sides of a right triangle. Calculate and
# show the length of the hypotenuse.
import math
opposite_side = float(input('Enter the value of opposite side of triangle:'))
adjacent_leg = float(input('Enter the value of adjacente leg of triangle:'))
hypotenuse = math.hypot(opposite_side,adjacent_leg)
print('The value of opposite side is {} and the value of adjacent leg is {}, its hypotenuse is {:.2f}.'.format(opposite_side, adjacent_leg, hypotenuse))
