import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def collision(self, other):
        # if the distance between two objects is less than the sum of their radii, there is a collision
        if (self.position.distance_to(other.position) < self.radius + other.radius):
            return True
        else:
            return False

    # subclasses will override the following
    def draw(self, screen):
        pass

    def update(self, dt):
        pass
