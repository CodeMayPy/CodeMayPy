preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção?'))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif preco == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
