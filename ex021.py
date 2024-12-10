# Write a Python program that opens and plays audio from an MP3 file.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('nana.mp3')
pygame.mixer.music.play()
pygame.quit()
