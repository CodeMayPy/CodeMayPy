# Write a program that reads a person's full name, then shows the first and last names separately.
name = str(input('Enter your full name:'))
value = name.split()
print('Muito prazer em te conhecer!')
print(f'Your first name is {value[0]}.')
print(f'Your last name is {value[len(value)-1]}.')
