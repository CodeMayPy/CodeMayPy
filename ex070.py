#070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = totmil = menor = cont =  0
barato = ' '
while True:
    produto = str(input('Qual o produto que você quer comprar?'))
    preco = float(input('Qual o valor do produto em R$:'))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print("Fim do programa.")
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
