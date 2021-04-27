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
    
    #VAR
    running = True 
    spawnBuff = 15
    
    #set up of pygame clock   
    clock = pygame.time.Clock()
    MAX_FPS = 20
    
    
    #patinet 0
    patient0 = Person(random.randint(spawnBuff, WIDTH-spawnBuff), random.randint(spawnBuff, HEIGHT-spawnBuff), "sick", False)
    
   
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#exited game 
                running = False   
       
        
         #up people
        patient0.update()
        
        #graphics update
        screen.fill(pygame.Color("gray"))
        patient0.draw(screen)
        pygame.display.flip()
    
        #frame counter
        clock.tick(MAX_FPS)
    
    pygame.quit()

        
main()