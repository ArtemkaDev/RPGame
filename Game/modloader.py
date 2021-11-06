import os

class mod():
    def __init__(self):
        pass

    def start(self):
        if os.path.exists("./mods") is False:
            os.mkdir("mods")

    '''def load(self):
        try:
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):'''