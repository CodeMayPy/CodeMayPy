#The National Swimming Confederation needs a program that reads an athlete's birth year and shows their
# category, according to age: – Up to 9 years old: child
#– Up to 14 years old: children's
#– Up to 19 years old: JUNIOR
#– Up to 25 years old: SENIOR
#– Over 25 years old: MASTER
from datetime import date
atual = date.today().year
birth = int(input('What year was the athlete born?'))
age = atual - birth
print(F'the athlete was born in {birth} and has {age} years old.')
if age <= 9:
    print('Your category is CHILD!')
if age >= 10 and age < 14:
    print("Your category is CHILDREN'S.")
if age >= 15 and age <= 19:
    print('Your category is JUNIOR!')
if age >= 20 and age <= 25:
    print('Your category is SENIOR!')
elif age >=26:
    print('Your category is MASTER!')
