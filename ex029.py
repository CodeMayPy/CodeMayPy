velocidade = float(input('Digite a velocidade do seu carro:'))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar uma multa de R${}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
