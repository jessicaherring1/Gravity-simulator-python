from turtle import position
from cv2 import sqrt
import pygame 
import random
import math

class Body:
    px = 0 #x position
    py = 0 #y position
    vx = 0 #x velocity 
    vy = 0 #y velocity
    ax = 0 #x acceleration
    ay = 0 #y acceleration 

    radius = 0
    mass =0
    angle = 0
    distance = 0
    orbitSpeed = 15
    bodies=[]

    isHit = False
    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0

    def __init__(self, tempH, tempW, tempmass, temppx=0, temppy=0, tempvx=0, tempvy=0,):
        self.h = tempH
        self.w = tempW
        self.mass = tempmass
        self.px=temppx
        self.py = temppy
        self.vx=tempvx
        self.vy = tempvy
        degree = random.randint(0, 360)
        self.angle = (degree * 2 * math.pi) / 360
        self.add_body(self)
    
    def render(self, aSurface):
        pygame.draw.circle(aSurface, (255, 0, 255), (self.px, self.py), self.h/2)
    
    def resetBoundaries(self): #incomplete
        self.topBound = self.y
        self.bottomBound = self.y + self.height

    def orbit(self):
        #angle += orbitSpeed
        pass

    def move(self):
        self.px = self.px + self.vx
        self.py = self.py + self.vy

    # functions used/adapted from 
    # https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/
    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    #both arguments must be a Body object
    '''
    def acceleration(body1, body2):
        tempDist = math.dist((body1.px, body1.py), (body2.px, body2.py))
        force = body1.mass * body2.mass / tempDist**2
        angle = math.atan2((body1.py - body2.py),(body1.px - body2.px))
        reverse = 1

        for body in body1, body2:
            acceleration = force / body.mass
            body.ax = acceleration * math.cos(math.radians(angle))
            body.ay = acceleration * math.sin(math.radians(angle))
            body.vx = body.vx + body.ax
            body.vy = body.vy + body.ay
            reverse = -1'''

    def acceleration(self, body2):
        dx = body2.px - self.px # change in two x-positions
        dy = body2.py- self.py # change in two y-positions
        d = math.sqrt(dx**2 + dy**2)

       
        
        if d != 0:
            force = (self.mass * body2.mass) / d**2
        else:
            force = 0
        theta = math.atan2(dy,dx)

        fx = math.cos(theta) * force
        fy = math.sin(theta) * force

        self.ax = (fx / self.mass) #* -1
        self.ay = (fy / self.mass) #*-1
        #print(self.ax, self.ay)
        
        self.vx += self.ax 
        self.vy += self.ay 
        self.px += self.vx
        self.py += self.vy
        
        body2.ax = (fx / body2.mass)*-1
        body2.ay = (fy / body2.mass)*-1
        #print(body2.ax, body2.ay)

        body2.vx += body2.ax
        body2.vy += body2.ay
        body2.px += body2.vx
        body2.py += body2.vy 
        '''
        self.ax = self.mass*(body2.px-self.px) / tempDist**2
        self.ay = self.mass*(body2.py-self.py) / tempDist**2

        body2.ax = body2.mass*(self.px-body2.px) / tempDist**2
        body2.ay = body2.mass*(self.py-body2.py) / tempDist**2

        self.vx = self.vx + self.ax
        self.vy = self.vy + self.ay
        self.px = self.px + self.vx
        self.py = self.py + self.vy

        body2.vx = body2.vx + (body2.ax * -1)
        body2.vy = body2.vy + (body2.ay * -1)
        body2.px = body2.px + body2.vx
        body2.py = body2.py + body2.vy

        selfAcceleration = force / self.mass
        self.ax = selfAcceleration * math.cos(math.radians(angle))
        self.ay = selfAcceleration * math.sin(math.radians(angle))
        self.vx = self.vx + self.ax
        self.vy = self.vy + self.ay
        self.px = self.px + self.vx
        self.py = self.py + self.vy
        reverse = -1

        body2Acceleration = force / body2.mass
        body2.ax = body2Acceleration * math.cos(math.radians(angle))
        body2.ay = body2Acceleration * math.sin(math.radians(angle))
        body2.vx = body2.vx + body2.ax
        body2.vy = body2.vy + body2.ay
        body2.px = body2.px + body2.vx
        body2.py = body2.py + body2.vy
        reverse = 1'''


    
    
