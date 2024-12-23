#22- Create a program that reads a person's full name and displays:
# - The name in all upper and lower case letters.
# - How many letters in total without considering spaces
# - How many letters are in the first name.
name = str(input('Enter your full name:'))
print('Analyzing your name...')
print(f'Your name in capital letters:{name.upper()}.')
print(f'Your name in lower case:{name.lower()}.')
print(f'Your name in total has {len(name)-name.count(' ')} letters.')
separate = name.split()
print(f'Your first name is {separate[0]} and he has {len(separate[0])} letters.')
