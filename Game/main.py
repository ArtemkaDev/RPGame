from modules.jsons import jsons
from modules.player import Solider
import pygame
import json
import os

#json
jsons().check()

with open(os.path.expanduser(f"{os.getenv('APPDATA')}\ProjectRedAdventure\config.json"), "r") as json_file:
    config_json = json.load(json_file)


#stats of screen
if config_json['screen']['mode'] == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
elif config_json['screen']['mode'] == 2:
    screen = pygame.display.set_mode((config_json['screen']['width'], config_json['screen']['height']))
else:
    print("Error")
clock = pygame.time.Clock()
fps = config_json['fps']

#stats of game
pygame.display.set_caption('ProjectRed Adventures')#game name
#create player
player = Solider(200, 200, 3, 5,screen)

moving_left = False
moving_right = False

#run
while True:
    clock.tick(fps)
    player.draw()
    player.move(moving_left, moving_right)
    for event in pygame.event.get():
        #quit game
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

    pygame.display.update() #update

pygame.quit()