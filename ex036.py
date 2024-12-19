#Write a program to approve a bank loan for the purchase of a house. Ask the buyer for the value of the house, the
# buyer's salary and in how many years he will pay it off. The monthly payment cannot exceed 30% of the salary or
# else the loan will be denied.

house = float(input('What is the value of the house you want to buy in R$:'))
salary = float(input('What is your salary in R$:'))
time = float(input('How many years do you want to pay off the house?'))
installment = house / (time * 12)
condition = salary * 0.30
print(f'To pay for a house R${house:.2f} in {time:.0f} years.')
print(f'The installment will be of R${installment:.2f}.')
if installment <= condition:
    print('Congratulations your loan was approved!')
else:
    print('Try adding one more income.')

'''
# code my friend "V
house = float(input('House value (R$): '))
salary = float(input('Salary (R$): '))
time = int(input('Years to pay: '))

installment = house / (time * 12)
condition = salary * 0.3

print(f'Installment: R${installment:.2f} | Limit: R${condition:.2f}')
print('Loan approved!' if installment <= condition else 'Loan denied! Increase income.'''

