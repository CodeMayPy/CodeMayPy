# Make a program that reads an employee's salary and shows his new salary with a 15% increase.
salary = float(input('Enter your salary in R$:'))
print('Calculating you new salary with a 15% increase...')
increase = salary + (salary * 0.15)
print(f'Your new salary will be R${increase}.')
