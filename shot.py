import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        print('shot init', x, y)
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def rotate(self, player_rotation):
        self.rotation += player_rotation
