#08- Write a program that reads a value in meters and displays it converted into centimeters and millimeters.
meter = int(input('Enter a value in meters:'))
print(f'''If this value is {meter}, converting it:
{meter/1000} km,
{meter/100} Hm,
{meter/10} Dam,
{meter*10} Dm,
{meter*100} Cm,
{meter*1000} Mm.''')
