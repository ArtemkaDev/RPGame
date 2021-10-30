from modules.player import Solider
from modules.jsons import jsons
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

BG = (144, 201, 120)


def draw_bg():
    screen.fill(BG)


# stats of game
pygame.display.set_caption('ProjectRed Adventures')  # game name


# fps
def display_fps():
    text_to_show = base_font.render(str(int(clock.get_fps())), 0, pygame.Color("white"))
    screen.blit(text_to_show, (10, 10))


# create player
player = Solider("default", 200, 600, 3, 5, screen)

# run
while True:
    clock.tick(fps)
    if authorizat:
        draw_bg()
        player.update_animation()
        player.draw()
        display_fps()
        if moving_left or moving_right:
            player.update_action(1)  # run
        else:
            player.update_action(0)  # stay

        player.move(moving_left, moving_right)
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                elif event.key == pygame.K_d:
                    moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                elif event.key == pygame.K_d:
                    moving_right = False
        pygame.display.update()  # update
    else:
        user_text = ''
        screen.fill(BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode



pygame.quit()
sys.exit()