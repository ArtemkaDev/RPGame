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

#stats of game
if type_screen == 1:
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
elif type_screen == 2:
    pygame.display.set_mode(())

#run
while True:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            break

pygame.quit()