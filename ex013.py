# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
s = float(input('Digite o valor do seu salário em R$:'))
print('Calculando seu novo salário com aumento de 15%...')
a = s + (s * 0.15)
print('Seu novo salário seá de R${}.'.format(a))
