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
