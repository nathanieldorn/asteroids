import pygame, random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.r = radius

    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_vector1 = self.velocity.rotate(split_angle)
        split_vector2 = self.velocity.rotate(split_angle * -1)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        old_position = self.position
        new_ast1 = Asteroid(old_position.x, old_position.y, new_radii)
        new_ast2 = Asteroid(old_position.x, old_position.y, new_radii)
        new_ast1.velocity = (split_vector1 * 1.2)
        new_ast2.velocity = (split_vector2 * 1.2)
