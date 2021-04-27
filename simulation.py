import pygame, random
#importing person class from virus code
from Virus.Person import Person

def main():
    pygame.init()
    #setup of pygame screen
    WIDTH = HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Simulation")
    screen.fill(pygame.Color("gray"))
    
    
    
    #set up of pygame clock   
    clock = pygame.time.Clock()
    MAX_FPS = 20
    
    
    #VAR
    running = True 
    spawnBuff = 15
    
    numpeople = 100
    #patinet 0
    patient0 = Person(random.randint(spawnBuff, WIDTH-spawnBuff), random.randint(spawnBuff, HEIGHT-spawnBuff), "sick", False)
    people = [patient0]
    socialDistancing = False
    for i in range(numpeople -1):

        if i < social_distancing_percentage*numpeople:
            socialDistancing=True
        colliding = True
        while colliding:
            person = Person(random.randint(spawnBuff,WIDTH-spawnBuff),random.randint(spawnBuffer,HEIGHT-spawnBuff),"healthy",False)
            colliding = False
            for person2 in people:
                if person.checkCollisionwithball(person2):
                    colliding =True
                    break
        people.append(person)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#exited game 
                running = False   
        for person in people:
            person.update(screen,people)
        screen.fill(pygame.Color("gray")) 
        for person in people:
            person.draw(screen)
        
         
       
        pygame.display.flip()
        #frame counter
        clock.tick(MAX_FPS)
    
       
       
    
        pygame.quit()    
main()