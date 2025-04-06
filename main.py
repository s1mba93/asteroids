import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    # Main Game Loop
    while True:
        # Check for the close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                raise SystemExit
            
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
        for asteroid in drawable:
         asteroid.draw(screen)
            
        pygame.display.flip()
        
        
        
        
        # Limit framerate
        dt = clock.tick(60) / 1000
        
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()