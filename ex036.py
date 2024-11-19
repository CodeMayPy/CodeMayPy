# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa que você deseja comprar em R$:'))
salario = float(input('Qual o seu salário em R$:'))
tempo = float(input('Em quantos anos você quer pagar a casa?'))
prestacao = casa / (tempo * 12)
condicao = salario * 0.30
print('Para pagar uma casa de R${} em {} anos.'.format(casa, tempo), end='')
print('A prestação será de R${}.'.format(prestacao))
if prestacao <= condicao:
    print('Parabéns foi aprovado o emprestimo!')
else:
    print('Tente adicionar mais uma renda')
