import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Group initialization
    updatable = pygame.sprite.Group() # Objects that can be updated
    drawable = pygame.sprite.Group() # Objects that can be drawn
    asteroids = pygame.sprite.Group() # Objects that are asteroids
    shots = pygame.sprite.Group() # Group of bullets

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group=shots)
    asteroid_field = AsteroidField()

    while True:
        # Check if user has closed the window, and close if yes 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) # Triple 0 for black screen
       
       
        updatable.update(dt)

        for drawing in drawable:
            drawing.draw(screen)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    bullet.kill()
                    print(bullet in shots)
                    asteroid.split()

            if player.check_collision(asteroid):
                print("Game over!")
                return
 
        pygame.display.flip()

        # FPS 60 seconds
        clock.tick(60)
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()