#Escreva um programa que converta uma temperatura digitando em graus Celsius para graus Fahrenheit.
c = int(input('Digite o valor da temperatura em graus Celcius:'.strip()))
f = ( c * 1.8) + 32
print('Se a temperatura local é de {}C convertendo ficará {:.2f}F.'.format(c, f))
