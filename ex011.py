# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
a = float(input('Digite a altura  em metros da parede que deseja pintar:'.strip()))
l = float(input('Agora digite a largura em metros da mesma:'.strip()))
area = a * l
litros = area / 2
print('Se você possui uma área de {}m logo precisará de {} litros para pintá-la.'.format(area, litros))
