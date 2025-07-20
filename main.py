import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    print(
        f"Starting Asteroids!\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #---Groups---
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    #---Containers----
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group,updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    
    my_player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),PLAYER_RADIUS, updatable_group, drawable_group)
    my_asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        # ---- Add shapes under here ----
        for sprite in drawable_group :
            sprite.draw(screen)
        updatable_group.update(dt)
        for asteroid in asteroid_group :
            if asteroid.collision(my_player) == True :
                print ("Game over!")
                return
            for shot in shot_group :
                if asteroid.collision(shot) == True :
                    asteroid.split()



        pygame.display.flip()
        dt = clock.tick(60) / 1000
      

if __name__ == "__main__":
    main()
