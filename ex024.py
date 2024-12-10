# Create a program that reads the name of a city and says whether or not it starts with the name 'Saint'.
city = str(input('What city were you born?')).strip()
print(city[:5].upper() == 'SAINT')
