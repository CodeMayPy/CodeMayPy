# Write a program that asks for an employee's salary and calculates the amount of his raise. For salaries
# above R$1,250.00, calculate an increase of 10% for those below or equal, the increase is 15%
salary = float(input('What is your salary in R$?'))
if salary <= 1250:
    new = salary + (salary * 0.15)
else:
    new = salary + (salary * 0.10)
print(f'Who won R${salary} starts to win R${new} now.')
