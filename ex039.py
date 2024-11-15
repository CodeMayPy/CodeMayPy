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
