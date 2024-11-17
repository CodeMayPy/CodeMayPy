# Crie um programa que leia um número e mostre seu antecessor e seu sucessor.
n = int(input('Digite um número:'.strip()))
print(f'Se o número escolhido foi \033[35m{n}\033[m, seu antecessor é \033[31m{(n-1)}\033[m e seu sucessor é \033[32m{(n+1)}\033[m.')
