import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.phase_timer = 0
        self.phase_cooldown = 0
        self.player_score = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.phase_shift() is True:
            player_triangle = pygame.draw.polygon(screen, (255, 255, 0), self.triangle(), 2)
        else:
            player_triangle = pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(dt * -1)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(dt * -1)
            if keys[pygame.K_SPACE]:
                if self.shoot_timer <= 0:
                    self.shoot(self.position)
                    self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            if keys[pygame.K_f]:
                if self.phase_timer <= 0 and self.phase_cooldown <= 0:
                    self.phase_shift()
                    self.phase_timer = PLAYER_SHOOT_COOLDOWN * 10
                    self.phase_cooldown = PLAYER_SHOOT_COOLDOWN * 100

            self.phase_cooldown -= dt
            self.phase_timer -= dt
            self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, position):
        bullet  = Shot(position.x, position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * 500

    def phase_shift(self):
        while self.phase_timer > 0:
            return True
        return False
