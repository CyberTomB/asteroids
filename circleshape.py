import pygame
from typing import ClassVar

class CircleShape(pygame.sprite.Sprite):
    position: ClassVar[pygame.Vector2]
    velocity: ClassVar[pygame.Vector2]

    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def is_in_collision(self, other) -> bool:
        distance_between = self.position.distance_to(other.position)
        return distance_between < self.radius + other.radius