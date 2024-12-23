#57- Make a program that reads a person's gender, but only accepts the values ​​'M' or 'F'. If it's wrong, ask
# typing again until you have a correct value.
gender = str(input('What is your gender?[F/M]:')).strip().upper()[0]
while gender not in 'MmFf':
    gender = str(input('Invalid data!! Please enter your gender:')).strip().upper[0]
print(f'Gender {gender} successfully registered.')
