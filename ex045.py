from random import randint
print('Vamos jogar pedra, papel ou tesoura:')
itens= ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('-=-' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0:
   if jogador == 0:
      print('Empate')
   elif jogador == 1:
       print('Jogador vence!')
   elif jogador ==2:
        print('Computador vence!')
   else:
       print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
      print('Computador vence!')
    elif jogador == 1:
      print('Empate')
    elif jogador == 2:
      print('Jogador vence!')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
       print('Jogador vence!')
    elif jogador == 1:
         print('Computador vence!')
    elif jogador == 2:
         print('empate')
    else:
        print('Jogada invalida!')
