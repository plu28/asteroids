import pygame as pg
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # groups are added to organize functionality per class
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # all further objects of the player class will be apart of these groups
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroid)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pg.time.Clock()

    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game loop is an infinite while loop
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.fill("black")

        # iterates over all objects in these groups and runs their corresponding functionality
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroid:
            if obj.collision(player):
                print("Game Over!")
                return
            for shot in shots:
                if obj.collision(shot):
                    obj.split()
                    shot.kill()
        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
