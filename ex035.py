#35-  Develop a program that reads the length of three straight lines and tells the user whether or not they can form a
# triangle.
print('-=-' * 20)
print('               Triangle analyzer...')
print('-=-' * 20)
first_segment =  float(input('First segment:'))
second_segment = float(input('Second segment:'))
third_segment = float(input('Third segmant:'))
if first_segment < second_segment + third_segment and second_segment < first_segment + third_segment and third_segment < first_segment + second_segment:
    print('The segments above CAN form a triangle.')
else:
    print('The segments above CANNOT form a triangle.')
