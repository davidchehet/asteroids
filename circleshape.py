import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Overriding subclasses
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    # Detect collisions of objects
    def check_collision(self, object):
        distance = self.position.distance_to(object.position)
        radii = self.radius + object.radius # Radius of two objects combined
        # Check for collision
        return radii >= distance