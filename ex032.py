#32- Make a program that reads any year and shows whether it is a leap year.
year = int(input('Which year do you want to analize?'))
if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
    print(f"The year {year} it's a leap year")
else:
    print(f"The year {year} it's not a leap year")
