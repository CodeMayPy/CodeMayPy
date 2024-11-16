# Crie um programa que leia a altura, a largura e diga quanto será usado de tinta para pinta-lá em l.
a = float(input('Digite a altura  em metros da parede que deseja pintar:'.strip()))
l = float(input('Agora digite a largura em metros da mesma:'.strip()))
area = a * l
litros = area / 2
print('Se você possui uma área de {}m logo precisará de {} litros para pintá-la.'.format(area, litros))
