import pygame

from constants import *
from player import Player

'''pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
starting_x = SCREEN_WIDTH / 2
starting_y = SCREEN_HEIGHT / 2
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
player1 = Player(starting_x, starting_y)'''

'''def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawable:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for item in updatable:
            updatable.update(dt)'''

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #game_loop()

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    starting_x = SCREEN_WIDTH / 2
    starting_y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(starting_x, starting_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000
        for upd in updatable:
            upd.update(dt)
        screen.fill("black")
        for drw in drawable:
            drw.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
