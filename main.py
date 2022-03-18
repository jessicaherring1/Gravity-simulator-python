import cv2
from cv2 import circle
import pygame
from Body import Body
from HandDetector import HandDetector



WIDTH = 1200
HEIGHT = 800

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulator")
FPS=60

planet = Body(15, 100, 15)

def main():
    clock = pygame.time.Clock()
    handDetector = HandDetector()

# make a boolean that represents whether the game should continue to run or not
    running = True


    # while the game is running
    while running:
        # this makes it so this function can run at most FPS times/sec
        clock.tick(FPS)

        # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
               pass

        WINDOW.fill((0,0,0))
        planet.render(WINDOW)

        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

        # put code here that should be run every frame
         # of your game             
        pygame.display.update()
main()