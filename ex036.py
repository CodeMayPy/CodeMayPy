#Write a program to approve a bank loan for the purchase of a house. Ask the buyer for the value of the house, the
# buyer's salary and in how many years he will pay it off. The monthly payment cannot exceed 30% of the salary or
# else the loan will be denied.
house = float(input('What is the value of the house you want to buy in R$:'))
salary = float(input('What is your salary in R$?:'))
time = float(input('How many years do you want to pay off the house?'))
installment = house / (time * 12)
condition = salary * 0.30
print(f'To pay for a house R${house} in {time} years.')
print(f'The installment will be of R${installment}.')
if installment <= condition:
    print('Congratulations your loan was approved!')
else:
    print('Try adding one more income.')
