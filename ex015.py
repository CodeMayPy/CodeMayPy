#Escreva um programa que pergunte a quantia de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = int(input('Digite quantos Km você rodou com o carro:'))
dia = int(input('Quantos dias você ficou com o carro:'))
vd = dia * 60
vkm = km * 0.15
print('Logo se você ficou {} dias com o carro e rodou {}Km com ele, logo você deverá pagar R${}.'.format(dia, km, (vd +vkm)))
