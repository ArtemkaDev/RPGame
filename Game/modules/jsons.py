import json
import os

#import pygame.image

player = 'img/Layer1.png'
appdata = os.getenv('APPDATA')
name = f"{appdata}\ProjectRedAdventure"
file_json = {
    "screen": {
        "mode": 1,
        "width": None,
        "height": None
    },
    "fps": 60
}

class jsons(object):
    def __init__(self):
        self.appdata = appdata
        self.name = name
        self.file_json = file_json
    def check(self):
        if os.path.exists(self.name) is False:
            os.mkdir(os.path.join(self.appdata, "ProjectRedAdventure"))
            os.system("attrib +h " + self.name)
            with open(f"{self.name}\config.json", "w+") as outfile:
                json.dump(self.file_json, outfile, indent=4)