#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 15% de desconto
produto = float(input('Digite o valor do produto em R$:'))
print('...Calculando seu desconto...')
desconto = produto - (produto * 0.15)
print('Seu produto de R${} com 15% de desconto ficará R${:.2f}'.format(produto, desconto))
