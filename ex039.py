# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
from xml.sax.handler import property_interning_dict

atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o seu alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
