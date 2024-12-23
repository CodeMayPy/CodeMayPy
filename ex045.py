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
