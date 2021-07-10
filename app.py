import pygame as pg
import os


pg.init()

APP_DIR = os.path.split(os.path.abspath(__file__))[0]
IMAGE_DIR = os.path.join(APP_DIR, 'images')


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 426
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon_image_path = os.path.join(IMAGE_DIR, 'icon.png')
icon_image = pg.image.load(icon_image_path)
pg.display.set_icon(icon_image)
pg.display.set_caption('Pygame Practice')
# pg.mouse.set_visible(False)

used_screen = [[0] * (SCREEN_HEIGHT + 1) for _ in range(SCREEN_WIDTH + 1)]

background_image_path = os.path.join(IMAGE_DIR, 'background.jpeg')
background_image = pg.image.load(background_image_path)

finish_image_path = os.path.join(IMAGE_DIR, 'finish.jpeg')
finish_image = pg.image.load(finish_image_path)

font = pg.font.Font(None, 80)
finish_text = font.render('FINISH', False, pg.Color('white'))


# player
player_image_path = os.path.join(IMAGE_DIR, 'icon.png')
player_image = pg.image.load(player_image_path)
player_x = 300
player_y = 300
PLAYER_WIDTH = 24
PLAYER_HEIGHT = 32

MOVE_DISTANCE = 1

# goal
goal_image_path = os.path.join(IMAGE_DIR, 'goal.png')
goal_image = pg.image.load(goal_image_path)
GOAL_WIDTH = 29
GOAL_HEIGHT = 32
goal_image = pg.transform.scale(goal_image, (GOAL_WIDTH, GOAL_HEIGHT))
goal_x = (SCREEN_WIDTH // 2) - (GOAL_WIDTH // 2)  # horizontal align center
goal_y = 0

for x in range(goal_x, goal_x + GOAL_WIDTH + 1):
    for y in range(goal_y, goal_y + GOAL_HEIGHT + 1):
        if not ((0 <= x <= SCREEN_WIDTH) and (0 <= y <= SCREEN_HEIGHT)):
            continue

        used_screen[x][y] = 2

# obstacle
obstacle_image_path = os.path.join(IMAGE_DIR, 'obstacle.png')
obstacle_image = pg.image.load(obstacle_image_path)
obstacle_rects = [(100, 100), (60, 250), (160, 320), (250, 120), (500, 220), (430, 50)]
OBSTACLE_WIDTH = 129
OBSTACLE_HEIGHT = 107

for obstacle_rect in obstacle_rects:
    obstacle_x = obstacle_rect[0]
    obstacle_y = obstacle_rect[1]
    for x in range(obstacle_x, obstacle_x + OBSTACLE_WIDTH + 1):
        for y in range(obstacle_y, obstacle_y + OBSTACLE_HEIGHT + 1):
            if not ((0 <= x <= SCREEN_WIDTH) and (0 <= y <= SCREEN_HEIGHT)):
                continue

            used_screen[x][y] = 1


def can_move(player_x: int, player_y: int):
    for x in range(player_x, player_x + PLAYER_WIDTH + 1):
        for y in range(player_y, player_y + PLAYER_HEIGHT + 1):
            if not ((0 <= x <= SCREEN_WIDTH) and (0 <= y <= SCREEN_HEIGHT)):
                continue

            if used_screen[x][y] == 1:
                return False

    return True


def reached_goal(player_x: int, player_y: int):
    for x in range(player_x, player_x + PLAYER_WIDTH + 1):
        for y in range(player_y, player_y + PLAYER_HEIGHT + 1):
            if not ((0 <= x <= SCREEN_WIDTH) and (0 <= y <= SCREEN_HEIGHT)):
                continue

            if used_screen[x][y] == 2:
                return True

    return False


finish = False
stop = False
while not stop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                stop = True

    if finish:
        screen.blit(finish_image, (0, 0))
        screen.blit(finish_text, (300, 180))
        pg.display.update()
        continue

    key_state = pg.key.get_pressed()
    tmp_player_rect = [player_x, player_y]
    if key_state[pg.K_UP]:
        tmp_player_rect[1] = player_y - MOVE_DISTANCE
    if key_state[pg.K_DOWN]:
        tmp_player_rect[1] = player_y + MOVE_DISTANCE
    if key_state[pg.K_LEFT]:
        tmp_player_rect[0] = player_x - MOVE_DISTANCE
    if key_state[pg.K_RIGHT]:
        tmp_player_rect[0] = player_x + MOVE_DISTANCE

    if can_move(tmp_player_rect[0], tmp_player_rect[1]):
        player_x, player_y = tmp_player_rect

    finish = reached_goal(player_x, player_y)

    screen.blit(background_image, (0, 0))
    screen.blit(goal_image, (goal_x, goal_y))
    screen.blit(player_image, (player_x, player_y))

    for obstacle_rect in obstacle_rects:
        screen.blit(obstacle_image, obstacle_rect)

    pg.display.update()


pg.quit()
