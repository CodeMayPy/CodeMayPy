#Body Mass Index
#43-Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI) and
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


#Índice de Massa Corporal
# 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
#seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o seu peso em KG:'))
altura = float(input('Qual é a sua altura em metros?'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif imc >= 18.5 and imc <25:
    print(f'Seu IMC é {imc:.2f} e você está no seu peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} e você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é de {imc:.2f} e você está com obesidade.')
elif imc > 40:
    print(f'Seu IMC é de {imc:.2f} e você está com obesidade mórbida.')


# PT- Condições aninhadas.
# EN- Aligned conditions.