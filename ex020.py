mport random
a1 = str(input('Digite o nome do primeiro aluno:'.strip()))
a2 = str(input('Digite o nome do segundo aluno:'.strip()))
a3 = str(input('Digite o nome do terceiro aluno:'.strip()))
a4 = str(input('Digite o nome do quarto aluno:'.strip()))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação dos alunos será:')
print(lista)
