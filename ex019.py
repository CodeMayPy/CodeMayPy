# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = str(input('Nome do primeiro aluno:'))
a2 = str(input('Nome do segundo aluno:'))
a3 = str(input('Nome do terceiro aluno:'))
a4 = str(input('Digite o nome do quarto aluno:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar o quadro é {}.'.format(escolhido))
