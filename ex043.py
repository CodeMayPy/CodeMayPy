#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input("Digite o seu peso em Kg:"))
altura = float(input('Digite a sua altura em metros:'))
imc = peso / (altura ** 2)
print('Seu peso é de {}kg e sua altura é de {}m, logo seu IMC é de {:.2f}.'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= 40:
    print('Você está obeso.')
elif imc >= 40:
    print('Você esta com obesidade mórbida.')
