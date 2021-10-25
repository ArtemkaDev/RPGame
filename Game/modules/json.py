import json
import os

appdata = os.getenv('APPDATA')
name = f"{appdata}\ProjectRedAdventure"
file_json = {
    "screen": {
        "mode": 1,
        "width": None,
        "height": None
    }
}

class json(object):
    def __init__(self):
        self.appdata = appdata
        self.name = name
        self.file.json = file_json

    def check(self):
        if os.path.exists(self.name):
            os.mkdir(os.path.join(self.appdata, "ProjectRedAdventure"))
            os.system("attrib +h " + self.name)
            with open(f"{self.name}\config.json", "w+") as f:
                json.dump(self.file_json, f)
    def __str__(self):
        with open(f"{self.name}\config.json", "r") as json_file:
            config_json = json.load(json_file)
        return config_json