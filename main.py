# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot
import pygame
import sys 



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable,drawable,shots)


    asteroid_field = AsteroidField()   
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    dt = 0 

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        

        updatable.update(dt)
        screen.fill("black")

        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                sys.exit()

        for obj in asteroids:
            for shot in shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()

        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        



if __name__ == "__main__":
    main()

