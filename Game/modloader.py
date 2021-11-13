import importlib
import os


class mod():
    def __init__(self, test):
        self.test = test
        self.mods_info = []

    def start(self):
        if not self.test:
            if os.path.exists("./mods") is False:
                os.mkdir("mods")

    def load(self):
        if not self.test:
            for filename in os.listdir("./mods"):
                if filename.endswith(".py"):
                    importlib.import_module(f".{filename[:-3]}", 'mods')
                    self.mods_info.append(f"{filename[:-3]}")