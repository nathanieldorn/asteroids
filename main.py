import pygame

from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000
        for upd in updatable:
            upd.update(dt)
        for coll in asteroids:
            if coll.collision(player1) is False:
                print("Game Over!")
                pygame.quit()
                return
        screen.fill("black")
        for drw in drawable:
            drw.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
