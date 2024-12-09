# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
dado = str(input('Digite seu nome completo:'))
nome = dado.split()
print('Muito prazer em te conhecer!')
print('Seu primeio nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
