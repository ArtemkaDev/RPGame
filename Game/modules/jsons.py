import json
import os

player = 'img/Layer1.png'
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
        self.appdata = os.getenv('APPDATA')
        self.name = f"{self.appdata}\ProjectRedAdventure"
        self.file_json = file_json
    def check(self):
        if os.path.exists(self.name) is False:
            os.mkdir(os.path.join(self.appdata, "ProjectRedAdventure"))
            os.system("attrib +h " + self.name)
            with open(f"{self.name}\config.json", "w+") as outfile:
                json.dump(self.file_json, outfile, indent=4)