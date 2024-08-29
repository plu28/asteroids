import pygame as pg
from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pg.time.Clock()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game loop is an infinite while loop
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
