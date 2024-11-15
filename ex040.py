n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua segunda nota:'))
media = ( n1 + n2 ) / 2
print('A sua média é {}.'.format(media))
if media < 5.0:
    print('Você foi REPROVADO!')
if media > 5.0:
    print('Você esta de REUPERAÇÂO!')
if media >= 6.9:
    print('Parabéns você passou!')
