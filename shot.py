import pygame
from constants import *
from player import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    # Override draw
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # Override update for constant, straight movement
    def update(self, dt):
        self.position += self.velocity * dt
