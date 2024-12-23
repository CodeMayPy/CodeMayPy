#31- Develop a program that asks the distance of a trip in km. Calculate the ticket price, charging R$0.50 per
#  km for trips up to 200km and R$0.45 for longer trips.
distance = float(input('What is the distance of your travel?'))
print(f'You wil stard a travel of {distance}km.')
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'And the price of your ticket will be R${price}.')
