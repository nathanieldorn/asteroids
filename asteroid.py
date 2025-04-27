import pygame, random

from circleshape import CircleShape
from constants import *
from player import Player

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

        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        elif self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

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
