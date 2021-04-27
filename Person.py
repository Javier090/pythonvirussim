import random

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
        pygame.draw.circle(screen, pygame.Color(self.color[self.status]), (round(self.x), round(self.y)), self.radius)

    #Update of the execution per frame of sick/recovery times
    def up(self):
        self.move()
        if self.status == "sick":
            self.turnSick += 1
        if self.turnSick == self.recoveryTime:
            self.status = "recovered"
        
        
    #movement of the "people" 
    def move(self):
        if not self.socialDistancing:
            self.x += self.vx
            self.y += self.vy
        