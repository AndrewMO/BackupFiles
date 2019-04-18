import pygame

pygame.init()
pygame.mixer.init()

six = pygame.mixer.Sound("A 6.wav")
six.set_volume(0.5)

sixlow = pygame.mixer.Sound("A b6.wav")
sixlow.set_volume(0.5)

seven = pygame.mixer.Sound("B 7.wav")
seven.set_volume(0.5)

sevenlow = pygame.mixer.Sound("B b7.wav")
sevenlow.set_volume(0.5)

onehigh = pygame.mixer.Sound("C 1#.wav")
onehigh.set_volume(0.5)

one = pygame.mixer.Sound("C 1(C).wav")
one.set_volume(0.5)

twohigh = pygame.mixer.Sound("D 2#.wav")
twohigh.set_volume(0.5)

two = pygame.mixer.Sound("D 2.wav")
two.set_volume(0.5)

threehigh = pygame.mixer.Sound("E 3#.wav")
threehigh.set_volume(0.5)

three = pygame.mixer.Sound("E 3.wav")
three.set_volume(0.5)

four = pygame.mixer.Sound("F 4.wav")
four.set_volume(0.5)

five = pygame.mixer.Sound("G 5.wav")
five.set_volume(0.5)

fivelow = pygame.mixer.Sound("G b5.wav")
fivelow.set_volume(0.5)
