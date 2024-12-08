# Write a program that reads something from the keyboard and shows its primitive type and all the
# possible information about him.
value = input('Type something:')
print('The primitive type of this value is:', type(value))
print('Is alphabetical?', value.isalpha())
print('Is a number?', value.isalnum())
print('There are only spaces?', value.isspace())
print('Is alphanumeric?', value.isalnum())
print('Is upper?', value.isupper())
print('is lower?', value.islower())
print('Only the first letter is capitalized?', value.istitle())
