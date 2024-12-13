# Improve the challenge 28 game where the computer will “think” of a number between 0 and 10. But now the player will
#try to guess until you get it right, showing at the end how many guesses it took to win.
from random import randint
computer = randint(0,10)
print('I am your computer. . . I just thought of a number between 0 and 10. ')
print('Can you guess which one it was?')
got_it_right = False
guesses = 0
while not got_it_right:
    player = (int(input('What is your guess?')))
    guesses +=1
    if player == computer:
        got_it_right = True
    else:
        if player < computer:
            print('More. Try again.')
        elif player > computer:
            print('Less. Try again.')
print(f'You got it rigth with {guesses} attempts. Congratulations!')