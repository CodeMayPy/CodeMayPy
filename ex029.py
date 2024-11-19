# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Digite a velocidade do seu carro:'))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar uma multa de R${}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
