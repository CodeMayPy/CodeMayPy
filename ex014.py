#Escreva um programa que converta uma temperatura digitando em graus Celsius para graus Fahrenheit.
celcius = int(input('Digite o valor da temperatura em graus Celcius:'))
fahrenheit = ( celcius * 1.8) + 32
print(f'Se a temperatura local é de {celcius}°C convertendo ficará {fahrenheit}°F.')
