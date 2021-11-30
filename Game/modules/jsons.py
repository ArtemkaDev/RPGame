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
            dif_json = jsondiff.diff(self.file_json, config_json)
            try:
                if isinstance(dif_json[jsondiff.delete], list):
                    for ix in range(len(dif_json)):
                        to_update = {f"{dif_json[jsondiff.delete][ix - 1]}": self.file_json[dif_json[jsondiff.delete][ix - 1]]}
                        config_json.update(to_update)
                    with open(os.path.expanduser(f"{self.name}\config.json"),
                              "w") as json_file:
                        json.dump(config_json, json_file, indent=4)
                    to_update = {}

                if isinstance(dif_json["screen"][jsondiff.delete], list):
                    nix_apend = {}
                    nix_apend.update(config_json["screen"])
                    for nix in range(len(dif_json["screen"][jsondiff.delete])):
                        nix_dif_update = dif_json["screen"][jsondiff.delete][nix - 1]
                        nix_type_update = {f"{nix_dif_update}": self.file_json["screen"][dif_json["screen"][jsondiff.delete][nix - 1]]}
                        nix_apend.update(nix_type_update)
                    to_update = {"screen": nix_apend}
                    print(to_update)
                    config_json.update(to_update)
                    with open(os.path.expanduser(f"{self.name}\config.json"),
                              "w") as json_file:
                        json.dump(config_json, json_file, indent=4)
                    to_update = {}

                with open(os.path.expanduser(f"{self.name}\config.json"), "r") as json_file:
                    config_json = json.load(json_file)
                dif_json = jsondiff.diff(self.file_json, config_json)
            except:
                pass

