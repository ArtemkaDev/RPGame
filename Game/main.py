import pygame
import json
import os

#folder in appdata
appdata = os.getenv('APPDATA')
name = f"{appdata}\ProjectRedAdventure"
file_json = {
    "screen": {
        "mode": 1,
        "width": None,
        "heigth": None
    }
}

if os.path.exists(name):
    os.mkdir(os.path.join(appdata, "ProjectRedAdventure"))
    os.system("attrib +h " + name)
    with open(f"{name}\config.json", "w+") as f:
        json.dump(file_json, f)

with open(f"{name}\config.json", "r") as json_file:
    config_json = json.load(json_file)

#stats of game
if config_json['screen']['mode'] == 1:
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
elif config_json['screen']['mode'] == 2:
    pygame.display.set_mode(())
else:
    print("Error")

#run
while True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            break

pygame.quit()