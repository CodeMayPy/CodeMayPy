# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input('Digite o nome do primeiro aluno:'.strip()))
a2 = str(input('Digite o nome do segundo aluno:'.strip()))
a3 = str(input('Digite o nome do terceiro aluno:'.strip()))
a4 = str(input('Digite o nome do quarto aluno:'.strip()))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação dos alunos será:')
print(lista)
