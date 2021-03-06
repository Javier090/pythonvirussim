import random
import math
import pygame


minMovement = 0.5
maximumS = 5


class Person():


    colors = {"healthy": "white", "sick": "red", "recovered": "green"}
    
    
    #used to describe the status of the person as healthy or sick
    def _init_(self, x, y, status, socialDistancing):
        self. x = x
        self. y = y 
        self.status = status 
        self.socialDistancing = socialDistancing
        self.radius = 5
        self.vx = self.vy = 0
        self.turnSick = 0
        self.recovertyTime = random.randint(10, 30)
        
        if not self.socialDistancing:
            while -minMovement < self.vx < minMovement and -minMovement < self.vy < minMovement:
                self.vx = random.uniform(-maximumS, maximumS)
                self.vy = random.uniform(-maximumS, maximumS)
    
    #surface aslo sets colors for circles that = people
    def draw(self, screen):            
        pygame.draw.circle(screen, pygame.Color(self.color[self.status]), (round(self.x), round(self.y)), self.radius, 5)

    #Update of the execution per frame of sick/recovery times
    def up(self):
        self.move()
        if self.status == "sick":
            self.turnSick += 1
        if self.turnSick == self.recoveryTime:
            self.status = "recovered"
            
#collisions
        self.checkCollision(screen)
        for other in people:
            if self != other:
                if self.checkCollisionwithball(other):
                    self.updateCollisionVelocity(other)
                    if self.status == "sick" and other.status == "healthy":
                        other.status = "sick"
                    elif other.status == "sick" and self.status == "healthy":
                        self.status = "sick"
        
        
    #movement of the "people depicted as either green balls if healthy or red if infected" 
    def move(self):
        if not self.socialDistancing:
            self.x += self.vx
            self.y += self.vy
    def checkCollision(self,screen):
        if self.x+self.radius>=screen.get_width() and self.vx>0:
            self.vx*=-1
        elif self.x-self.radius<=0 and self.vx<0:
            self.vx*= -1
        if self.y+self.radius>= screen.get_height() and self.vy>0:
            self.vy*=-1
        elif self.y -self.radius <=10 and self.vy <0:
            self.vy*= -1
    #people collision
def checkCollisionwithball(self,other):
    distance = math.sqrt(math.pow(self.x-other.x,2)+math.pow(self.y-other.y,2))
    if distance <= self.radius +other.radius:
        return True
    return False
#collision velovity
def updateCollisionVelocity(self,other):
        #type1 collision - both collision is social distancing
        if not self.socialDistancing and not other.socialDistancing:
            tempVX=self.vx
            tempVY=self.vy
            self.vx=other.vx
            self.vy=other.vy
            other.vx =tempVX
            other.vy =tempVY
        elif other.socialDistancing:
            magV = math.sqrt(math.pow(self.vx,2)+math.pow(self.vy,2))
            tempVector =(self.vx+(self.x -other.x),self.vy +(self.y-other.y))
            magTemVector =math.sqrt(math.pow(tempVector[0],2)+ math.pow(tempVector[1],2))
            normTempvector = (tempVector[0]/magTemVector,tempVector[1]/magTemVector)
            self.vx = normTempvector[0]*magV
            self.vy = normTempvector[1]*magV
#check for collision with ball 
def checkCollision(self,other):
    distance = math.sqrt(math.pow(self.x-other.x,2)+math.pow(self.y-other.y,2))
    if distance <= self.radius +other.radius:
        return True
    return False
def updateCollisionVelocity(self,other):
        #socially distanced people
        if not self.socialDistancing and not other.socialDistancing:
            tempVX=self.vx
            tempVY=self.vy
            self.vx=other.vx
            self.vy=other.vy
            other.vx =tempVX
            other.vy =tempVY
        elif other.socialDistancing:
            magV = math.sqrt(math.pow(self.vx,2)+math.pow(self.vy,2))
            tempVector =(self.vx+(self.x -other.x),self.vy +(self.y-other.y))
            magTemVector =math.sqrt(math.pow(tempVector[0],2)+ math.pow(tempVector[1],2))
            normTempvector = (tempVector[0]/magTemVector,tempVector[1]/magTemVector)
            self.vx = normTempvector[0]*magV
            self.vy = normTempvector[1]*magV
