from modules.jsons import jsons
import pygame
import json
import os

player = 'img/Layer 1.png'

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
x = 200
y = 200
img = pygame.image.load(player)
rect = img.get_rect()
rect.center = (x, y)
#load player
screen.blit(img, rect)

#run
while True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            break
    pygame.display.update() #update

pygame.quit()