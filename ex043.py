#Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI) and
# shows their status, according to the table below:
# – BMI below 18.5: Underweight
#– Between 18.5 and 25: Ideal Weight
#– 25 to 30: Overweight
#– 30 to 40: Obesity
#– Over 40: Morbidly Obese
weight = float(input("Enter your weight in Kg:"))
height = float(input('Enter your height in meters:'))
bmi = weight / (height ** 2)
print(f'Your weight is {weight}kg and your height is {height}m, your BMI is {bmi:.2f}.')
if bmi < 18.5:
    print('You are underweight.')
elif 18.5 <= bmi < 25:
    print('You are ideal weight!')
elif 25 <= bmi < 30:
    print('You are overweight.')
elif 30 <= 40:
    print('You are obesity.')
elif bmi >= 40:
    print('You are morbidly obese.')
