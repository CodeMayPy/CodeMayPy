# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerando US$ 1,00 = R$5.45
real = float(input('Quanto dinheiro você tem na sua carteira em R$:'.strip()))
dollar = real/5.45
print('Logo se voc~e tem R${} você poderá comprar US${:.2f}.'.format(real, dollar))
