# Write a program that asks the number of km traveled by a rented car and the number of days for which
# it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.
km = int(input(' Enter how many Km you have driven the car:'))
day = int(input('How many days did you keep the car:'))
value_day = day * 60
value_km = km * 0.15
print('If you stayed {} days with the carand it ran {}Km with him, then you must pay R${}.'.format(day, km, (value_day +value_km)))
