# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
area_q = float(input('Digite a altura  em metros da parede que deseja pintar:'))
largura = float(input('Agora digite a largura em metros da mesma:'))
area = area_q * largura
litros = area / 2
print(f'Se você possui uma área de {area}m logo precisará de {litros} litros para pintá-la.')
