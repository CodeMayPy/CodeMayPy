#GAME: Rock Paper Scissors
#45-Create a program that makes the computer play Jokenpô with you.
from random import randint
print("Let's play rock, paper, scissors:")
items= ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors''')
player = int(input("What's your move?"))
print('-=-' * 11)
print(f'Computer played {items[computer]}.')
print(f'Player played {items[player]}.')
print('-=-' * 11)
if computer == 0:
   if player == 0:
      print('Draw')
   elif player == 1:
       print('Player win!')
   elif player ==2:
        print('Computer win!')
   else:
       print('Invalid move!')
elif computer == 1:
    if player == 0:
      print('Computer win!')
    elif player == 1:
      print('Draw')
    elif player == 2:
      print('Player win!')
    else:
        print('Invalid move!')
elif computer == 2:
    if player == 0:
       print('Player win!')
    elif player == 1:
         print('Computer win!')
    elif player == 2:
         print('Draw')
    else:
        print('Invalid move!')


#GAME: Pedra Papel e Tesoura
#45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('Vamos jogar jokenpô')
items= ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada?'))
print(f'computador jogou {items[computador]}.')
print(f'Você jogou {items[jogador]}.')
if computador == 0:
   if jogador == 0:
      print('Empate.')
   elif jogador == 1:
       print('Você ganhou!')
   elif jogador == 2:
        print('Computador ganhou!')
   else:
       print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
      print('Computador ganhou!')
    elif jogador == 1:
      print('Empate!')
    elif jogador == 2:
      print('Você ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
       print('Você ganhou!')
    elif jogador == 1:
         print('Computador ganhou!')
    elif jogador == 2:
         print('Empate!')
    else:
        print('Jogada inválida!')


#PT- Condições aninhadas.
#EN- Aligned conditions.