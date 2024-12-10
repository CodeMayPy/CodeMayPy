# Create an algorithm that reads the price of a product and shows its new price with a 15% discount
product = float(input('Enter a price of a product R$:'))
print('...Calculating the discount...')
discount = product - (product * 0.15)
print('Your product R${} with 15% of discount will be R${:.2f}'.format(product, discount))
