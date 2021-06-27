import pygame as pg
import os


pg.init()

APP_DIR = os.path.split(os.path.abspath(__file__))[0]
IMAGE_DIR = os.path.join(APP_DIR, 'images')


screen = pg.display.set_mode((640, 480))

icon_path = os.path.join(IMAGE_DIR, 'icon.png')
icon_image = pg.image.load(icon_path)
pg.display.set_icon(icon_image)
pg.display.set_caption('Pygame Practice')
# pg.mouse.set_visible(False)

background_image_path = os.path.join(IMAGE_DIR,'background.jpeg')
background_image = pg.image.load(background_image_path)
screen.blit(background_image, (0, 0))
pg.display.flip()

running = True
while running:
    for even in pg.event.get():
        if even.type == pg.QUIT:
            running = False


pg.quit()
