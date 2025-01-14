#Approving Loan
#36-Write a program to approve a bank loan for the purchase of a house. Ask the buyer for the value of the house, the
# buyer's salary and in how many years he will pay it off. The monthly payment cannot exceed 30% of the salary or
# else the loan will be denied.

'''house = float(input('What is the value of the house you want to buy in R$:'))
salary = float(input('What is your salary in R$:'))
time = float(input('How many years do you want to pay off the house?'))
installment = house / (time * 12)
condition = salary * 0.30
print(f'To pay for a house R${house:.2f} in {time:.0f} years.')
print(f'The installment will be of R${installment:.2f}.')
if installment <= condition:
    print('Congratulations your loan was approved!')
else:
    print('Try adding one more income.')'''


#Aprovando Empréstimo
#36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa que deseja comprar?'))
salario = float(input('Qual o seu salário?'))
tempo = float(input('Em quanto tempo você deseja pagar a casa?'))
parcela = casa / (tempo * 12)
condicao = salario * 0.30
if parcela <= condicao:
    print('Empréstimo liberado.')
else:
    print('Tente adicionar mais uma renda')

#PT- Condições aninhadas.
#EN- Aligned conditions.