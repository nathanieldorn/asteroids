import pygame

from pygame.time import Clock
from constants import *
from player import Player

pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
starting_x = SCREEN_WIDTH / 2
starting_y = SCREEN_HEIGHT / 2
player1 = Player(starting_x, starting_y)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player1.update(dt)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop()

if __name__ == "__main__":
    main()
