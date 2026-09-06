import pygame
pygame.init()
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play()
pygame.event.wait()
while pygame.mixer.music.get_busy():
    pass