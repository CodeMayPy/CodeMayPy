# Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try
# find out which number was chosen by the computer. The program should write on the screen whether the user won or
# it lost.
from random import randint
computer = randint(0, 5)
print('-=-' * 20)
print('I will think of a number from 0 to 5, try guess...')
print('-=-' * 20)
player = int(input('What number did I think of?'))
if player == computer:
    print('CONGRATULATIONS! You beat me.')
else:
    print(f'I WON!!!!! I thought about the number {computer} and not in {player}!')
