# crie um programa que calcule o seno, cosseno e a tangente.
import math
ang = float(input('Digite o valor de um ângulo qualquer:'))
seno = math.sin(math.radians(ang))
print('O valor do SENO é {:.2f}.'.format(seno))
cos = math.cos(math.radians(ang))
print('O valor do COSSENO é {:.2f}'.format(cos))
tan = math.tan(math.radians(ang))
print('O valor da TANGENTE é de {:.2f}'.format(tan))
