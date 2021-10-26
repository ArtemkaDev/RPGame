from modules.jsons import jsons
import pygame
import json
import os

player = 'img/Layer 1.png'

jsons().check()

with open(os.path.expanduser(f"{os.getenv('APPDATA')}\ProjectRedAdventure\config.json"), "r") as json_file:
    config_json = json.load(json_file)

#stats of game
if config_json['screen']['mode'] == 1:
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('ProjectRed Adventures')#game name
    #create player
    x = 200
    y = 200
    img = pygame.image.load(player)
    rect = img.get_rect()
    rect.center = (x, y)
    #load player
    config_json['screen'].blit(img, rect)#AttributeError: 'dict' object has no attribute 'blit'

elif config_json['screen']['mode'] == 2:
    pygame.display.set_mode((config_json['screen']['width'], config_json['screen']['height']))
else:
    print("Error")

#run
while True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            break
    pygame.display.update()#update

pygame.quit()