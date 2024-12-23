#46- Make a program that displays a countdown on the screen for fireworks to go off, going from 10 to 0,
# with a 1 second pause between them.
from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('Bum! Bum! POOOOW!')
