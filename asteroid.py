import pygame
from constants import *
from player import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override draw
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Override update for constant, straight movement
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: # Small asteroid, take it away fully
            return
        else:
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-1 * angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2

