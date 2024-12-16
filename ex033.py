# Write a program that reads three numbers and shows which is the largest and which is the smallest.
first_value = int(input('Enter the first value:'))
second_value = int(input('Enter the second value:'))
third_value = int(input('Enter the tirth value:'))
smallest = first_value
if second_value < first_value and second_value < third_value:
    smallest = second_value
if third_value < first_value  and third_value < second_value:
    smallest = third_value
largest = first_value
if second_value > first_value and second_value > third_value:
    largest = second_value
if third_value > first_value and third_value > second_value:
    largest = third_value
print(f'The smallest value is {smallest}.')
print(f'The largest value is {largest}.')
