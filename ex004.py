# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
a = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(a))
print('É alfabetico?', a.isalpha())
print('É numerico?', a.isalnum())
print('Só tem espaços?', a.isspace())
print('É alfanumerico?', a.isalnum())
print('Está em maiúsculo?', a.isupper())
print('Esta em minúsculo?', a.islower())
print('Esta só com a primeira letra em maiúsculo?', a.istitle())
