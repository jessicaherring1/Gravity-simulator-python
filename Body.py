import pygame 
import random
import math

class Body:
    vx = 0 #change the intial to a different number 
    vy = 0 #change the intial to a different number 
    ax = 0
    ay = 0
    #x = 0
    #y = 0

    radius = 20
    angle = 0
    distance = 0
    orbitSpeed = 15


    width = 20
    height = 20
    speed = 0
    isHit = False
    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0

    def __init__(self, tempr, tempd, tempo):
        self.radius = tempr
        self.distance = tempd
        self.orbitSpeed = tempo
        degree = random.randint(0, 360)
        angle = (degree * 2 * math.pi) / 360
    
    def render(self, aSurface):
        #body = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(aSurface, (255, 0, 255), body)
        pygame.draw.circle(aSurface, (255, 0, 255), (600, 600), self.radius)
    def resetBoundaries(self): #incomplete
        self.topBound = self.y
        self.bottomBound = self.y + self.height

    def orbit(self):
        #angle += orbitSpeed
        pass

