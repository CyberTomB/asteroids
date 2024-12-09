import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    global dt
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)


    # Establish players
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            for s in shots:
                if(a.is_in_collision(s)):
                    s.kill()
                    a.split()
            if(a.is_in_collision(player)):
                print("Game Over!")
                pygame.quit()
                    
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()