p = float(input('Digite o valor do produto em R$:'.strip()))
print('...Calculando seu desconto...')
d = p - (p * 0.15)
print('Seu produto de R${} com 15% de desconto ficará R${:.2f}'.format(p, d))
