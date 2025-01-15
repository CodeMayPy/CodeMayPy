#Military draft
#39- Write a program that reads the year of birth of a young person and informs, according to his age, whether he is
# still going to enlist in the military service, whether it is the exact time to enlist or if it is past the
# enlistment period. Your program should also show the time remaining or the time that has passed.
'''from datetime import date

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
    print(f'You should have enlisted {result} years ago.')'''


#Alistamento Militar
#39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
#alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
#deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Qual o seu ano de nascimento?'))
ano = date.today().year
idade = ano - ano_nascimento
print(f'Se você nasceu em {ano_nascimento} a sua idade é {idade}.')
if idade == 18:
    print('Você deve se alistar.')
elif idade < 18:
    print(f'Você ainda tem {18 - idade} aos até se alistar.')
elif idade > 18:
    print(f'Já passou {idade - 18} do prazo de alistamento')


#PT- Condições aninhadas.
#EN- Aligned conditions.