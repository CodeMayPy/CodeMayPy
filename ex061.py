#61-  Redo CHALLENGE 51, reading the first term and the reason of an AP, 
showing the first 10 terms of the progression
#  using the while structure.
print("Arithmetic progression generator")
print("-=-" * 20)
first_term = int(input("Enter the first term:"))
reason = int(input("Enter the reason of the arithmetic progression:"))
term = first_term
counter = 1
while counter <= 10:
    print(f"{term}", end=' ')
    term += reason
    counter += 1
print("End")
