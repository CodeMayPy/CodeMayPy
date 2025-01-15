#Ranking Athletes
#41-The National Swimming Confederation needs a program that reads an athlete's birth year and shows their
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


#Classificando Atletas
#041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input('Qual o seu ano de nascimento?'))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'Sua idade é {idade} então sua categoria é a mirim.')
if idade > 9 and idade <= 14:
    print(f'Sua idade é {idade} então sua categoria é a infantil.')
if idade  > 14 and idade <= 19:
    print(f'Sua idade é {idade} então sua categoria é a junior.')
if idade > 19 and idade <= 25:
    print(f'Sua idade é {idade} então sua categoria é a sênior.')
elif idade >= 26:
    print(f'Sua idade é {idade} e sua categoria é a master.')


#PT- Condições aninhadas.
#EN- Aligned conditions.