#10- Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
#  Considering US$1.00 = R$5.45
real = float(input('How much many do you have in R$:'))
dollar = real/5.45
print('So if you have R${} you can buy US${:.2f}.'.format(real, dollar))
