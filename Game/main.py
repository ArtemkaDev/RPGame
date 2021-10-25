from modules.json import json
import pygame

config_json = json.check()

#stats of game
if config_json['screen']['mode'] == 1:
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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

pygame.quit()