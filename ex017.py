# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o valor do cateto oposto do triângulo:'))
ca = float(input('Digite o valor do cateto adjacente do triângulo:'))
hi = math.hypot(co,ca)
print('O valor do cateto oposto é {} e o do cateto adjacente é {}, logo a sua hipotenusa é {:.2f}.'.format(co, ca, hi))
