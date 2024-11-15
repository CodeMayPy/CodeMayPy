km = int(input('Digite quantos Km você rodou com o carro:'.strip()))
dia = int(input('Quantos dias você ficou com o carro:'))
vd = dia * 60
vkm = km * 0.15
print('Logo se você ficou {} dias com o carro e rodou {}Km com ele, logo você deverá pagar R${}.'.format(dia, km, (vd +vkm)))
