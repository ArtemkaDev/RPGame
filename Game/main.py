from modules.jsons import jsons
from modules.player import Solider
import pygame
import json
import os

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
#stats of game
pygame.display.set_caption('ProjectRed Adventures')#game name
#create player
player = Solider(200, 200, 3)

#load player
screen.blit(player.img, player.rect)

#run
while True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            break
    pygame.display.update() #update

pygame.quit()