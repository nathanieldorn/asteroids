import pygame
from pygame.sprite import WeakDirtySprite

from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.phase_timer = 0
        self.phase_cooldown = 0
        self.warp_cooldown = 0
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
            if self.warp_cooldown > 0:
                forward = pygame.Vector2(0, 1).rotate(self.rotation)
                right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
                engine_1 = self.position - forward * self.radius - right
                engine_2 = self.position - forward * self.radius + right
                engine_overheat = pygame.draw.line(screen, (255, 0, 0), (engine_1), (engine_2), 2)

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
                    self.phase_timer = PLAYER_SHOOT_COOLDOWN * 10
                    self.phase_cooldown = PLAYER_SHOOT_COOLDOWN * 100
                    self.phase_shift()
            if keys[pygame.K_q]:
                if self.warp_cooldown <= 0:
                    self.warp_cooldown = PLAYER_SHOOT_COOLDOWN * 50
                    self.warp_jump(self.position)

            self.phase_cooldown -= dt
            self.warp_cooldown -= dt
            self.phase_timer -= dt
            self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        elif self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

    def shoot(self, position):
        bullet  = Shot(position.x, position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * 500

    def phase_shift(self):
        while self.phase_timer > 0:
            return True
        return False

    def warp_jump(self, position):
        position.x = SCREEN_WIDTH - position.x
        position.y = SCREEN_HEIGHT - position.y
