from modules.player import Solider
from modules.jsons import jsons
from pygame import Color
import pygame
import json
import sys
import os

pygame.font.init()

# value
in_game = False
# сделать то что снизу на False когда сделаешь авторизацию
authorizat = True
# сверху
moving_left = False
moving_right = False
base_font = pygame.font.SysFont("Futura", 48)

# json
jsons().check()

with open(os.path.expanduser(f"{os.getenv('APPDATA')}\ProjectRedAdventure\config.json"), "r") as json_file:
    config_json = json.load(json_file)

# stats of screen
if config_json['screen']['mode'] == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF, 16)
elif config_json['screen']['mode'] == 2:
    screen = pygame.display.set_mode((config_json['screen']['width'], config_json['screen']['height']))
else:
    print("Error")

clock = pygame.time.Clock()
fps = config_json['fps']

# background
BG = (144, 201, 120)


def draw_bg():
    screen.fill(BG)
    p1 = (300, 1920)
    p2 = (0, 1920)
    # pygame.draw.line(screen, Color("red"), p1, p2, width=3)


# stats of game
pygame.display.set_caption('ProjectRed Adventures')  # game name


# fps
def display_fps():
    screen.blit(base_font.render(str(int(clock.get_fps())), 0, pygame.Color("white")), (10, 10))


# create player
player = Solider("default", 200, 600, 3, 10, screen)


# stop
def stop():
    pygame.quit()
    sys.exit()


# input
user_text = ''

# run
stop_run: bool = False



if __name__ == '__main__':
    while True:
        if stop_run:
            stop()
            break
        elif authorizat:
            while True:
                #draw
                draw_bg()
                player.update_animation()
                player.draw()
                display_fps()
                pygame.display.update()  # update
                #event
                if player.alive:
                    if moving_left or moving_right:
                        player.update_action(1)  # run
                    else:
                        player.update_action(0)  # stay
                # quit game
                for event_reject in pygame.event.get():
                    if event_reject.type == pygame.QUIT:
                        stop_run = True
                    elif event_reject.type == pygame.KEYDOWN:
                        if event_reject.key == pygame.K_a:
                            moving_left = True
                        elif event_reject.key == pygame.K_ESCAPE:
                            stop_run = True
                        elif event_reject.key == pygame.K_d:
                            moving_right = True
                        elif event_reject.key == pygame.K_SPACE and player.alive:
                            player.jump = True
                    elif event_reject.type == pygame.KEYUP:
                        if event_reject.key == pygame.K_a:
                            moving_left = False
                        elif event_reject.key == pygame.K_d:
                            moving_right = False
                        elif event_reject.key == pygame.K_SPACE:
                            player.jump = False
                player.move(moving_left, moving_right)
                if stop_run:
                    break
                clock.tick(fps)
            continue
        else:
            while True:
                screen.fill(BG)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        stop()
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
                clock.tick(fps)
            continue
