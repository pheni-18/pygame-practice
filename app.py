import pygame as pg
import os


pg.init()

APP_DIR = os.path.split(os.path.abspath(__file__))[0]
IMAGE_DIR = os.path.join(APP_DIR, 'images')


screen = pg.display.set_mode((640, 426))

icon_image_path = os.path.join(IMAGE_DIR, 'icon.png')
icon_image = pg.image.load(icon_image_path)
pg.display.set_icon(icon_image)
pg.display.set_caption('Pygame Practice')
# pg.mouse.set_visible(False)

background_image_path = os.path.join(IMAGE_DIR,'background.jpeg')
background_image = pg.image.load(background_image_path)

player_image_path = os.path.join(IMAGE_DIR, 'icon.png')
player_image = pg.image.load(player_image_path)
player_x = 300
player_y = 300

MOVE_DISTANCE = 5

stop = False
while not stop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                stop = True
            if event.key == pg.K_UP:
                player_y -= MOVE_DISTANCE
            if event.key == pg.K_DOWN:
                player_y += MOVE_DISTANCE
            if event.key == pg.K_LEFT:
                player_x -= MOVE_DISTANCE
            if event.key == pg.K_RIGHT:
                player_x += MOVE_DISTANCE

    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    pg.display.update()


pg.quit()
