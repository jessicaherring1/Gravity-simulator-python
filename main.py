import cv2
from cv2 import circle
import pygame
from Body import Body
from HandDetector import HandDetector
import math

#surfaces/window/screeens stuff
WIDTH = 1092 #window width
HEIGHT = 610 #window height
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("background1.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

home = pygame.image.load("home.png").convert()
home = pygame.transform.scale(home, (WIDTH, HEIGHT))

blankHome = pygame.image.load("blank.jpg").convert()
blankHome = pygame.transform.scale(blankHome, (WIDTH, HEIGHT))

instructions1 = pygame.image.load("instructions1.png").convert()
instructions1 = pygame.transform.scale(instructions1, (WIDTH, HEIGHT))

instructions2 = pygame.image.load("instructions2.png").convert()
instructions2 = pygame.transform.scale(instructions2, (WIDTH, HEIGHT))

instructions3 = pygame.image.load("instructions3.png").convert()
instructions3 = pygame.transform.scale(instructions3, (WIDTH, HEIGHT))

instructions4 = pygame.image.load("instructions4.png").convert()
instructions4 = pygame.transform.scale(instructions4, (WIDTH, HEIGHT))


#planets
p1 = pygame.image.load("planet1.png").convert_alpha()
p1 = pygame.transform.scale(p1, (45, 45))
p1H = p1.get_height()
p1W = p1.get_width()

p2 = pygame.image.load("planet2.png").convert_alpha()
p2 = pygame.transform.scale(p2, (150, 150))
p2H = p2.get_height()
p2W = p2.get_width()

p3 = pygame.image.load("planet3.png").convert_alpha()
p3 = pygame.transform.scale(p3, (60, 60))
p3H = p3.get_height()
p3W = p3.get_width()

p4 = pygame.image.load("planet4.png").convert_alpha()
p4 = pygame.transform.scale(p4, (85, 85))
p4H = p4.get_height()
p4W = p4.get_width()

p5 = pygame.image.load("planet5.png").convert_alpha()
p5 = pygame.transform.scale(p5, (100, 100))
p5H = p5.get_height()
p5W = p5.get_width()

p6 = pygame.image.load("planet6.png").convert_alpha()
p6 = pygame.transform.scale(p6, (115, 115))
p6H = p6.get_height()
p6W = p6.get_width()

#user hand
openHand = pygame.image.load("openHand.JPG").convert_alpha()
openHand = pygame.transform.scale(openHand, (50, 50))
closedHand = pygame.image.load("closedHand.JPG").convert_alpha()
closedHand = pygame.transform.scale(closedHand, (50, 50))


#pygame stuff
pygame.display.set_caption("Gravity Simulator")
FPS=60

#Bodies
planet1 = Body(p1H, p1W, 10, 800, 250, 4, 4)
planet2 = Body(p2H, p2W, 10000, 450, 250)
planet3 = Body(p3H, p3W, 20, 300, 300, 1, 1)
planet4 = Body(p4H, p4W, 30, 350, 350, 1, 2)
planet5 = Body(p5H, p5W, 40, 500, 100, 2, 2)
planet6 = Body(p6H, p6W, 50, 450, 50, 2, 1)

bodies = {planet1, planet2, planet3, planet4, planet5, planet6}

collision = False





####################
# function defs
####################
def mapToNewRange(val, inputMin, inputMax, outputMin, outputMax):
    return outputMin + ((outputMax - outputMin) / (inputMax - inputMin)) * (val - inputMin)


###################
# main func 
###################
def main():
    clock = pygame.time.Clock()
    handDetector = HandDetector()

    #state/switch mode
    state = 6

    #timers
    startTime = pygame.time.get_ticks()
    endTime = 0
    interval = 1000

    # make a boolean that represents whether the game should continue to run or not
    running = True

    #circle Vars
    circleX = 0
    circleY = 0
    circleZ =0
    circleC = (0, 255, 255)

    handIsOpen=True
    handIsClosed=False

    # while the game is running
    while not handDetector.shouldClose and running:
        # this makes it so this function can run at most FPS times/sec
        handDetector.update()

        clock.tick(FPS)

        if state == 0: #planet intro
            screen.blit(blankHome, [0,0])

        if state ==1: #home screen
            screen.blit(home, [0,0])

        if state == 2: # instructions 1
            screen.blit(instructions1, [0,0])
            if len(handDetector.landmarkDictionary) > 0:
                if (handDetector.landmarkDictionary[0][12][1]) <(handDetector.landmarkDictionary[0][9][1]):
                    handIsOpen = True
                else:
                    handIsOpen = False

        if state == 3: # instructions 2
            screen.blit(instructions2, [0,0])

        if state == 4: # instructions 3
            screen.blit(instructions3, [0,0])
            if len(handDetector.landmarkDictionary) > 0:
                if (handDetector.landmarkDictionary[0][12][1]) <(handDetector.landmarkDictionary[0][9][1]):
                    handIsClosed = False
                else:
                    handIsClosed = True

        if state == 5: # instructions 4
            screen.blit(instructions4, [0,0])

        if state == 6: # gravity sim

            screen.blit(bg, [0,0])

            if len(handDetector.landmarkDictionary) > 0:
                circleX = handDetector.landmarkDictionary[0][9][0]
                circleY = handDetector.landmarkDictionary[0][9][1]
                circleZ = 30

                #mirror circleX/Y so its more intuitive
                circleX = WIDTH - mapToNewRange(circleX, 0, 640, 0, WIDTH)
                circleY = mapToNewRange(circleY, 0, 480, 0, HEIGHT)

                #draw circle at point 9
                #pygame.draw.circle(WINDOW, (255, 0, 255), (circleX, circleY), circleZ)

                if (handDetector.landmarkDictionary[0][12][1]) <(handDetector.landmarkDictionary[0][9][1]):
                    handIsOpen = True
                    #circleC = (0, 255, 255)
                else:
                    handIsOpen = False
                    #circleC = (255, 0, 0)

                # update hitbox
                handTop = circleY - circleZ
                handBottom = circleY + circleZ
                handLeft = circleX - circleZ
                handRight = circleX + circleZ

                for body in bodies:
                    planetTop = body.py# - body.radius
                    planetBottom = body.py + body.h#body.radius
                    planetLeft = body.px #- body.radius
                    planetRight = body.px + body.w#body.radius
                    
                    
                    if planetLeft <= handRight and planetTop <= handBottom and planetRight >= handLeft and planetBottom >= handTop:
                        collision = True
                        circleC = (0, 255, 0)

                        # if hand is closed, then make planet stick to hand
                        if not handIsOpen:
                            hold = True
                            circleC = (0, 0, 255)
                            body.px= circleX - (body.w / 2)
                            body.py = circleY - (body.h / 2)

                    else:
                        #planet1.acceleration(planet2)  #fix
                        print(planet1.px)
                        circleC = (0, 255, 255)
                    
                    for body2 in bodies:
                        planet2Top = body2.py
                        planet2Bottom = body2.py + body2.h
                        planet2Left = body2.px 
                        planet2Right = body2.px + body2.w
                        if body != body2:
                            if planetLeft <= planet2Right and planetTop <= planet2Bottom and planetRight >= planet2Left and planetBottom >= planet2Top:
                                planetCollision = True
                                '''
                                if body.mass > body2.mass:
                                    bodies.remove(body2)
                                else:
                                    bodies.remove(body)
                                '''
            
            for body in bodies:
                for body1 in bodies:
                    if(body!=body1):
                        savex =planet2.px
                        savey = planet2.py
                        body.gravity(body1)
                        planet2.px = savex
                        planet2.py= savey 

            # TODO- DELETE ME- IM A TEST
            # planet1.acceleration(planet2)
            #planet2.gravity(planet1)
            #planet2.gravity(planet3)

            #planet1.gravity(planet2)  
            #planet2.gravity(planet1)  
            # planet3.acceleration(planet2)  
            # planet4.acceleration(planet2)  
            # planet5.acceleration(planet2)  
            # planet6.acceleration(planet2) 
            # planet2.px = 450
            # planet2.py= 250 
            print(planet1.px)

            #planet2.gravity(planet1)
            # for body in bodies:
            #     for body1 in bodies:
            #         if(body!=body1):
            #             body.gravity(body1)
            #             planet2.px = 450
            #             planet2.py= 250
            '''
                planetTop = planet.py - planet.radius
                planetBottom = planet.py + planet.radius
                planetLeft = planet.px - planet.radius
                planetRight = planet.px + planet.radius

                planet1Top = planet1.py - planet1.radius
                planet1Bottom = planet1.py + planet1.radius
                planet1Left = planet1.px - planet1.radius
                planet1Right = planet1.px + planet1.radius
                
                
                if planetLeft <= handRight and planetTop <= handBottom and planetRight >= handLeft and planetBottom >= handTop:
                    collision = True
                    circleC = (0, 255, 0)

                    if not handIsOpen:
                        hold = True
                        circleC = (0, 0, 255)
                        planet.px= circleX - (p1W / 2)
                        planet.py = circleY - (p1H / 2)

                if planet1Left <= handRight and planet1Top <= handBottom and planet1Right >= handLeft and planet1Bottom >= handTop:
                    collision = True
                    circleC = (0, 255, 0)
                    
                    if not handIsOpen:
                        hold = True
                        circleC = (0, 0, 255)
                        planet1.px= circleX - (p1W / 2)
                        planet1.py = circleY - (p1H / 2)

                else:
                    planet.acceleration(planet1) '''

                

        # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False 
        
        
        if state == 2:
            if handIsOpen:
                #delay
                state = 3

        if state == 3:
            endTime = pygame.time.get_ticks()
            if endTime - startTime >= interval:
                state = 4
                startTime = pygame.time.get_ticks()
            

        if state ==4 and handIsClosed:
            state = 5
        
        if state == 5:
            endTime = pygame.time.get_ticks()
            if endTime - startTime >= interval:
                state = 6
        

        if state==6:
            #planet1.render(WINDOW)
            
            #planet1.move()
            #planet2.render(WINDOW)
            screen.blit(p2, (planet2.px, planet2.py))
            screen.blit(p1, (planet1.px, planet1.py))
            #planet2.move()
            screen.blit(p3, (planet3.px, planet3.py))
            screen.blit(p4, (planet4.px, planet4.py))
            screen.blit(p5, (planet5.px, planet5.py))
            screen.blit(p6, (planet6.px, planet6.py))
            if len(handDetector.landmarkDictionary) > 0:
                if handIsOpen:
                    screen.blit(openHand, (circleX, circleY))
                else:
                    screen.blit(closedHand, (circleX, circleY))
            else:
                screen.blit(openHand, (circleX, circleY))

            
            #pygame.draw.circle(WINDOW, circleC, (circleX, circleY), circleZ)
        
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()
            
        pygame.display.update()
    
    # Closes all the frames
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()