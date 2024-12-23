#39- Write a program that reads the year of birth of a young person and informs, according to his age, whether he is
# still going to enlist in the military service, whether it is the exact time to enlist or if it is past the
# enlistment period. Your program should also show the time remaining or the time that has passed.
from datetime import date
from xml.sax.handler import property_interning_dict

year = date.today().year
birth = int(input('Enter your year of birth:'))
age = year - birth
print(f'Who was born in {birth} is {age} years old.')
if age == 18:
    print('You must enlist IMMEDIATELY!!')
elif age < 18:
    result = 18 - age
    print(f'Still missing {result} years for your enlistment.')
elif age > 18:
    result = age - 18
    print(f'You should have enlisted {result} years ago.')
