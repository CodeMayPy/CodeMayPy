#That Average classic.
#40- Create a program that reads two grades from a student and calculates their average, displaying a message at the end, according to the acquired media:
# – Media below 5.0: FAILED
# – AVERAGE BETWEEN 5.0 and 6.9: RECOVERED
# – Media 7.0 or higher: PASSED
first_note = float(input('Enter your note:'))
second_note = float(input('Enter the second note:'))
grade = ( first_note + second_note ) / 2
print(f'Your avarege is {grade}.')
if grade < 5.0:
    print('You are FAILED!')
if grade > 5.0:
    print('You are RECOVERED!')
if grade >= 6.9:
    print('Congratulations you PASSED!')


#Aquele clássico da Média.
# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota = float(input('Digite sua primeira nota:'))
segunda_nota = float(input('Digite sua segunda nota:'))
media = (nota + segunda_nota) / 2
if media < 5.0:
    print('Você está reprovado.')
if media >= 5.0 and media < 6.9:
    print('Você está de recuperação.')
if media >= 7.0:
    print('Parabéns você passou.')


#PT- Condições aninhadas.
#EN- Aligned conditions.