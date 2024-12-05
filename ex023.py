#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}.')
print(f'Sua unidade é {u}.')
print(f'Sua dezena é {d}.')
print(f'Sua centena é {c}.')
print(f'Seu milhar é {m}.')
