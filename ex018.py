# Write a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.
import math
angle = float(input('Enter a value of an angle:'))
sine = math.sin(math.radians(angle))
print('The value of sine is {:.2f}.'.format(sine))
cosine = math.cos(math.radians(angle))
print('The value of cosine is {:.2f}'.format(cosine))
tangent = math.tan(math.radians(angle))
print('The value of tangent is {:.2f}'.format(tangent))
