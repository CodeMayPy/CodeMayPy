# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nas= int(input(f'Em que ano a {pessoas}ª pessoa nasceu?'))
    idade = atual - nas
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print(f' Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E {totmenor} pessoas menores de idade.')
