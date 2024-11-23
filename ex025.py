#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Qual é o seu nome completo?'))
print('Seu nome tem Silva? {}.'.format('silva' in nome.lower()))
