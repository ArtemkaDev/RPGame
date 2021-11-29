import jsondiff
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

    def write_json(self):
        with open(f"{self.name}\config.json", "w+") as outfile:
            json.dump(self.file_json, outfile, indent=4)

    def check(self):
        if os.path.exists(self.name) is False:
            os.mkdir(os.path.join(self.appdata, "ProjectRedAdventure"))
            os.system("attrib +h " + self.name)
            self.write_json()
        elif os.path.exists(f"{self.name}\config.json") is False:
            self.write_json()
        elif os.path.exists(self.name):
            if os.stat(f"{self.name}\config.json").st_size == 0:
                self.write_json()
            with open(os.path.expanduser(f"{self.name}\config.json"), "r") as json_file:
                config_json = json.load(json_file)
            try:
                dif_json = jsondiff.diff(self.file_json, config_json)[jsondiff.delete]
                for ix in range(len(dif_json)):
                    if dif_json[ix - 1] == "screen":
                        to_update = {f"{dif_json[ix - 1]}": self.file_json[dif_json[ix - 1]]}
                    else:
                        to_update = {f"{dif_json[ix - 1]}": self.file_json[dif_json[ix - 1]]}
                    config_json.update(to_update)
                    with open(os.path.expanduser(f"{self.name}\config.json"),
                              "w") as json_file:
                        json.dump(config_json, json_file, indent=4)
            except:
                try:
                    dif_json = jsondiff.diff(self.file_json, config_json)[jsondiff.delete]
                    for ix in range(len(dif_json)):
                        if dif_json[ix - 1] == "screen":
                            to_update = {f"{dif_json[ix - 1]}": self.file_json[dif_json[ix - 1]]}
                        else:
                            to_update = {f"{dif_json[ix - 1]}": self.file_json[dif_json[ix - 1]]}
                        config_json.update(to_update)
                        with open(os.path.expanduser(f"{self.name}\config.json"),
                                  "w") as json_file:
                            json.dump(config_json, json_file, indent=4)
                except:
                    pass


    def read(self):
        with open(os.path.expanduser(f"{os.getenv('APPDATA')}/ProjectRedAdventure/config.json"), "r") as json_file:
            return json.load(json_file)
