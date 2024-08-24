import pygame as pg
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop is an infinite while loop
    while True:
        screen.fill((0,0,0))
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

if __name__ == "__main__":
    main()
