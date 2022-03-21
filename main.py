import cv2
from cv2 import circle
import pygame
from Body import Body
from HandDetector import HandDetector
import math

import random


WIDTH = 1200 #window width
HEIGHT = 800 #window height
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("background.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

pygame.display.set_caption("Gravity Simulator")
FPS=60

planet = Body(30, 10, 600, 200, 2, 2)
planet1 = Body(60, 10000, 600, 400)

collision = False

def mapToNewRange(val, inputMin, inputMax, outputMin, outputMax):
    return outputMin + ((outputMax - outputMin) / (inputMax - inputMin)) * (val - inputMin)

def main():
    clock = pygame.time.Clock()
    handDetector = HandDetector()

# make a boolean that represents whether the game should continue to run or not
    running = True

    #circle Vars
    circleX = 0
    circleY = 0
    circleZ =0
    circleC = (0, 255, 255)

    handIsOpen=True

    # while the game is running
    while not handDetector.shouldClose and running:
        # this makes it so this function can run at most FPS times/sec
        handDetector.update()

        clock.tick(FPS)
 
        screen.blit(bg, [0,0])

        if len(handDetector.landmarkDictionary) > 0: 
            #print(handDetector.landmarkDictionary[0])
            circleX = handDetector.landmarkDictionary[0][9][0]
            circleY = handDetector.landmarkDictionary[0][9][1]
            #circleZ = handDetector.landmarkDictionary[0][9][2]
            #circleZ = abs(circleZ *5)
            circleZ = 30

            #mirror circleX/Y so its more intuitive
            circleX = WIDTH - mapToNewRange(circleX, 0, 640, 0, WIDTH)
            circleY = mapToNewRange(circleY, 0, 480, 0, HEIGHT)

            #draw circle at point 9
            pygame.draw.circle(WINDOW, (255, 0, 255), (circleX, circleY), circleZ)

            if (handDetector.landmarkDictionary[0][12][1]) <(handDetector.landmarkDictionary[0][9][1]):
                handIsOpen = True
                #circleC = (0, 255, 255)
            else:
                handIsOpen = False
                #circleC = (255, 0, 0)

            handTop = circleY - circleZ
            handBottom = circleY + circleZ
            handLeft = circleX - circleZ
            handRight = circleX + circleZ

            planetTop= planet.py - planet.radius
            planetBottom= planet.py + planet.radius
            planetLeft= planet.px - planet.radius
            planetRight= planet.px + planet.radius

            planet1Top= planet1.py - planet1.radius
            planet1Bottom= planet1.py + planet1.radius
            planet1Left= planet1.px - planet1.radius
            planet1Right= planet1.px + planet1.radius
            
            
            if planetLeft <= handRight and planetTop <= handBottom and planetRight >= handLeft and planetBottom >= handTop:
                collision = True
                circleC = (0, 255, 0)

                if not handIsOpen:
                    hold = True
                    circleC = (0, 0, 255)
                    planet.px= circleX
                    planet.py = circleY

            if planet1Left <= handRight and planet1Top <= handBottom and planet1Right >= handLeft and planet1Bottom >= handTop:
                collision = True
                circleC = (0, 255, 0)
                
                if not handIsOpen:
                    hold = True
                    circleC = (0, 0, 255)
                    planet1.px= circleX
                    planet1.py = circleY

            else:
                planet.acceleration(planet1)

                    
            '''
            #check collision between rectangle and hand point 
            if planet.collidepoint(circleX, circleY) or planet1.collidepoint(circleX, circleY):
                rectColor = (255,255, 0)
                if not handIsOpen:
                    rectColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                rectColor = (255, 0, 255)
            '''

        # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False 
        

        planet.render(WINDOW)
        #planet.move()
        planet1.render(WINDOW)
        #planet1.move()
        

        pygame.draw.circle(WINDOW, circleC, (circleX, circleY), circleZ)
        
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()
            
        pygame.display.update()
    
    # Closes all the frames
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()