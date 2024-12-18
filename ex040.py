# Create a program that reads two grades from a student and calculates their average, displaying a message at the end, according to the acquired media:
# – Media below 5.0: FAILED
# – AVERAGE BETWEEN 5.0 and 6.9: RECOVERED
# – Media 7.0 or higher: PASSED
first_note = float(input('Enter your note:'))
second_note = float(input('Enter the second note:'))
grade = ( first_note + second_note ) / 2
print(f'Your avarege is {grade}.')
if grade < 5.0:
    print('You are FAILED!')
if grade > 5.0:
    print('You are RECOVERED!')
if grade >= 6.9:
    print('Congratulations you PASSED!')
