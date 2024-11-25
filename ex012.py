#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 15% de desconto
preco = float(input('Digite o valor do produto em R$:'))
print('...Calculando seu desconto...')
dinheiro = preco - (preco * 0.15)
print(f'Seu produto de R${preco} com 15% de desconto ficará R${dinheiro}')
