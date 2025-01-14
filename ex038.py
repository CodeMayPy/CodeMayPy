#Comparing numbers
#38- Write a program that reads two integers and compares them, displaying a message on the screen:
# – The first value is greater
# – The second value is greater
# – There is no greater value, both are equal
first_number = int(input('Enter an integer:'))
second_number = int(input('Enter other integer:'))
if first_number > second_number:
    print(f'The number {first_number} is greater than {second_number}.')
elif first_number < second_number:
    print(f'The number {second_number} is greater than {first_number}.')
else:
    print('The two numbers are the same!')


#Comparando números
#38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
primeiro = int(input('Digite um número:'))
segundo = int(input('Digite outro número:'))
if primeiro > segundo:
    print(f'O número {primeriro} é maior que {segundo}.')
elif segundo > primeiro:
    print(f'O número {segundo} é maior que {primeiro}.')
else:
    print('Os dois números são iguais.')

#PT- Condições aninhadas.
#EN- Aligned conditions.