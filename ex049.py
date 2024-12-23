#49- Redo CHALLENGE 9, showing the multiplication table of a number that the user chooses, but now using a for loop.
number = int(input('Enter a number to showing the multiplication:'))
for c in range (1,11):
    print(f'{number} x {c:2} = {number * c}.')
