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
