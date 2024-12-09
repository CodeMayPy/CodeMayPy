# Write a program that reads the width and height of a wall in meters, calculates the amount of paint needed to
#  paint it, knowing that each liter of paint paints an area of 2m².
area_q = float(input('Enter the height in meters of the wall you want to paint:'))
width = float(input('Now enter the width in meters of the same:'))
area = area_q * width
liter = area / 2
print(f'If you have an area of {area}m soon you will need {liter} liters to paint it.')
