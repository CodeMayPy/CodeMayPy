# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
