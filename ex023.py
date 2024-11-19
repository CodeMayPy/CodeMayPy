#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Sua unidade é {}.'.format(u))
print('Sua dezena é {}.'.format(d))
print('Sua centena é {}.'.format(c))
print('Seu milhar é {}.'.format(m))
