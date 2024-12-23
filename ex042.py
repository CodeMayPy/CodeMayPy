#42- Redo triangle challenge 35, adding the feature of showing what type of triangle will be formed:
# – EQUILATERAL: all sides equal
# – ISOSCELES: two sides equal, one different
# – SCALENE: all sides different
first_segment = float(input('Enter thr first segment:'))
second_segment = float(input('Enter the second segment:'))
tirdh_segment = float(input('Enter the tirdh segment:'))
if first_segment < second_segment + tirdh_segment and second_segment < first_segment + tirdh_segment and tirdh_segment < first_segment + second_segment:
    print('The segments above CAN form a triangle!', end=' ')
    if first_segment == second_segment == tirdh_segment:
        print('Equilateral!')
    elif first_segment != second_segment != tirdh_segment != first_segment:
        print('Scalene!')
    else:
        print('Isosceles.')
else:
    print('The segments above CAN NOT form a triangle!.')
