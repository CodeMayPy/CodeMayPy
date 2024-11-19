#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:  – Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do nascimento do atleta?'))
idade = atual - nasc
print('O atleta nasceu em {} e tem {}anos.'.format(nasc, idade))
if idade <= 9:
    print('Sua categoria é a MIRIM!')
if idade >= 9 and idade < 14:
    print('Sua categoria é a INFANTIL!')
if idade >= 14 and idade <= 19:
    print('Sua categoria é a JÚNIOR!')
if idade >= 19 and idade <= 25:
    print('Sua categoria é a SÊNIOR!')
elif idade >=25:
    print('Sua categoria é a MASTER!')
