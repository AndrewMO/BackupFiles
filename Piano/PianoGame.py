import pygame
import sys
from pygame.locals import *
import sound
import cv2

"""
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
"""
image = pygame.image.load("piano.png")
image_rect = image.get_rect()

img = cv2.imread('piano.png')
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
SIZE = (width, height)

screen = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Piano Game")

note = pygame.image.load("the crotchets.png")
note_rect = note.get_rect()
quaver = pygame.image.load("quaver.png")
quaver_rect = note.get_rect()



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        screen.blit(image,image_rect)

        pygame.display.flip()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                sound.fivelow.play()
                quaver_rect.left,quaver_rect.top = 5,(image_rect.height - quaver_rect.height-30)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()

            if event.key == K_1:
                sound.sixlow.play()
                note_rect.left,note_rect.top = 90,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()
                
            if event.key == K_2:
                sound.sevenlow.play()
                quaver_rect.left,quaver_rect.top = 165,(image_rect.height - quaver_rect.height-15)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()
            
            if event.key == K_3:
                sound.one.play()
                note_rect.left,note_rect.top = 250,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()

            if event.key == K_4:
                sound.two.play()
                quaver_rect.left,quaver_rect.top = 325,(image_rect.height - quaver_rect.height)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()

            if event.key == K_5:
                sound.three.play()
                note_rect.left,note_rect.top = 415,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()

            if event.key == K_6:
                sound.four.play()
                quaver_rect.left,quaver_rect.top = 485,(image_rect.height - quaver_rect.height-30)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()

            if event.key == K_7:
                sound.five.play()
                note_rect.left,note_rect.top = 575,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()

            if event.key == K_8:
                sound.six.play()
                quaver_rect.left,quaver_rect.top = 650,(image_rect.height - quaver_rect.height-15)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()

            if event.key == K_9:
                sound.seven.play()
                note_rect.left,note_rect.top = 735,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()

            if event.key == K_0:
                sound.onehigh.play()
                quaver_rect.left,quaver_rect.top = 815,(image_rect.height - quaver_rect.height)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()

            if event.key == K_MINUS:
                sound.twohigh.play()
                note_rect.left,note_rect.top = 900,(image_rect.height - note_rect.height)
                screen.blit(note,note_rect)
                pygame.display.flip()

            if event.key == K_EQUALS:
                sound.threehigh.play()
                quaver_rect.left,quaver_rect.top = 975,(image_rect.height - quaver_rect.height-30)
                screen.blit(quaver,quaver_rect)
                pygame.display.flip()
                
        
        clock.tick(30)
