#50- Develop a program that reads six integers and displays the sum of only those that are even. If the value
# entered is odd, disregard it.
sum_numbers = 0
counter = 0
for c in range (1, 7):
    numbers = int(input(f'Enter a {c} value:'))
    if sum_numbers % 2 == 0:
        sum_numbers += numbers
        counter += 1
print(f"You informed {counter} neven numbers the sum was {sum_numbers}.")
