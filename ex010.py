# Crie um programa que leia o valor do real e o converta para dolar, considerando o dolar US$ 5,45.
real = float(input('Quanto dinheiro você tem na sua carteira em R$:'.strip()))
dollar = real/5.45
print('Logo se voc~e tem R${} você poderá comprar US${:.2f}.'.format(real, dollar))
