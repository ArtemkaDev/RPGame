from modules.player import Solider
from modules.jsons import jsons
import socket
import pygame
import json
import os

# value
servers = ("192.168.0.101", 5000)
in_game = False
# сделать то что снизу на False когда сделаешь авторизацию
authorizat = True
# сверху
moving_left = False
moving_right = False

# network
host = socket.gethostbyname(socket.gethostname())
port = 0

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
server.setblocking(0)

# json
jsons().check()

with open(os.path.expanduser(f"{os.getenv('APPDATA')}\ProjectRedAdventure\config.json"), "r") as json_file:
    config_json = json.load(json_file)

# stats of screen
if config_json['screen']['mode'] == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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


# create player
player = Solider(200, 600, 3, 5, screen)


# run
while True:
    clock.tick(fps)
    if authorizat:
        if moving_left or moving_right:
            player.update_action(1) #run
        else:
            player.update_action(0) #stay
        draw_bg()
        player.update_animation()
        player.draw()
        player.move(moving_left, moving_right)
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
        pygame.display.update()  # update
    else:
        pass

pygame.quit()
