#Payment Manager
#44- Develop a program that calculates the amount to be paid for a product, considering its normal price and
# payment conditions: – cash/check: 10% discount
#– cash on card: 5% discount
#– up to 2x on card: formal price
#– 3x or more on card: 20% interest
price = float(input('Purchase price:'))
print(''' PAYMENT METHODS:
[ 1 ] cash/pix in cash
[ 2 ] cash card
[ 3 ] 2x on card
[ 4 ] 3x or more on card''')
option = int(input('What is your option?'))
if option == 1:
    total = price - (price * 0.10)
elif option == 2:
    total = price - (price * 0.05)
elif price == 3:
    total = price
    installment = total / 2
    print(f'Your purchase will be paid in 2 installments of U${installment:.2f}interest free.')
elif option == 4:
    total = price + (price * 0.20)
    total_installment = int(input('How many installments?'))
    installment = total / total_installment
    print(f'Your purchase will be paid in installments {total_installment}x of U${installment:.2f}.')
print(f'Your purchase of U${price:.2f} it will cost U${total:.2f}.')


#Gerenciador de Pagamentos
#44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/pix: 10% de desconto
# débito : 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
preco = float(input('Qual o valor da sua compra R$:'))
print('''Qual a forma de pagamento?
[ 1 ] à vista (dinheiro ou pix)
[ 2 ] à vista (cartão de débito)
[ 3 ] 2x cartão de crédito
[ 4 ] 3x ou mais cartão de crédito''')
escolha = int(input('Qual a forma de pagamento?'))
if escolha == 1:
    print(f'Sua compra de R${preco} receberá desconto de 10% e ficará R${preco - (preco*0.10):.2f}.')
elif escolha == 2:
    print(f'Sua compre de R${preco} no débito ganha 5% de desconto e fica R${preco - (preco*0.05):.2f}.')
elif escolha == 3:
    print(f'Sua compre de R${preco} parcelada em 2x ficará em duas parcelas de R${preco/2:.2f}.')
elif escolha == 4:
    print(f'Sua compra de R${preco} em 3x ou mais terá a adição de 20% de juros e ficará no total R${preco +(preco*0.20):.2f}.')


#PT- Condições aninhadas.
#EN- Aligned conditions.