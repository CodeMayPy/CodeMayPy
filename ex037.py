#Number Base Converter
#37-Write a Python program that reads any integer and asks the user to choose the conversion base: 1 for binary, 2 for
# octal, and 3 for hexadecimal
number= int(input('Enter an integer:'))
print('''Choose one of the bases for conversion:
[ 1 ] convert to  BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL''')
option = int(input('your choose:'))
if option == 1:
    print(f'{number} converted to binary it becomes {bin(number)[2:]}.')
elif option == 2:
    print(f'{number} converted to octal it becomes {oct(number)[2:]}.')
elif option == 3:
    print(f'{number} converted to hexadecimal it becomes {hex(number)[2:]}.')
else:
    print('Invalid option try again!')



#Conversor de Bases Numéricas
#37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro qualquer:'))
print('''Escolha uma das bases de conversão:
      [ 1 ] BINÁRIO'
      [ 2 ] OCTAL'
      [ 3 ] HEXADECIMAL''')
opcao = int(input('Digite sua escolha:'))
if opcao == 1:
    print(f'o número {numero} convertido para binário fica: {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'O número {numero} convertido para octal fica: {oct(numero)[2:]}.')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal fica: {hex(numero)[2:]}.')
else:
    print('Opção inválida, tente novamente.')


#PT- Condições aninhadas.
#EN- Aligned conditions.