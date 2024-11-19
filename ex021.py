# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('nana.mp3')
pygame.mixer.music.play()
pygame.quit()
