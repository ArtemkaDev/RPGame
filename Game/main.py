from modules.player import Solider
from modules.jsons import jsons
from launcher import launcher
import modloader
import pygame
import json
import sys
import os

pygame.init()

# value
test_mod = True
in_game = False
# сделать то что снизу на False когда сделаешь авторизацию
authorizat = True
# сверху
moving_left = False
moving_right = False
base_font = pygame.font.SysFont("Futura", 48)

def init():
    global config_json
    global screen
    global clock
    global fps
    global player
    jsons().check()

    with open(os.path.expanduser(f"{os.getenv('APPDATA')}\ProjectRedAdventure\config.json"), "r") as json_file:
        config_json = json.load(json_file)

    if config_json['screen']['mode'] == 1:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF, 16)
    elif config_json['screen']['mode'] == 2:
        screen = pygame.display.set_mode((config_json['screen']['width'], config_json['screen']['height']), pygame.RESIZABLE)
    else:
        print("Error")

    pygame.display.set_caption('ProjectRed Adventures')

    clock = pygame.time.Clock()
    fps = config_json['fps']
    player = Solider("default", 200, 600, 3, 10, screen)


def draw_bg():
    screen.fill((144, 201, 120))
    p1 = (300, 1920)
    p2 = (0, 1920)
    # pygame.draw.line(screen, Color("red"), p1, p2, width=3)


#mod
modloader.mod(test_mod).start()
modloader.mod(test_mod).load()



# stop
def stop():
    pygame.quit()
    sys.exit()


# input
user_text = ''

# run
stop_run: bool = False



if __name__ == '__main__':
    while True:
        if stop_run:
            stop()
            break
        elif authorizat:
            init()
            while True:
                #draw
                draw_bg()
                player.update_animation()
                player.draw()
                screen.blit(base_font.render(str(int(clock.get_fps())), 0, pygame.Color("white")), (10, 10))
                pygame.display.update()  # update
                #event
                if player.alive:
                    if moving_left or moving_right:
                        player.update_action(1)  # run
                    else:
                        player.update_action(0)  # stay
                # quit game
                for event_reject in pygame.event.get():
                    if event_reject.type == pygame.QUIT:
                        stop_run = True
                    elif event_reject.type == pygame.KEYDOWN:
                        if event_reject.key == pygame.K_a:
                            moving_left = True
                        elif event_reject.key == pygame.K_ESCAPE:
                            stop_run = True
                        elif event_reject.key == pygame.K_d:
                            moving_right = True
                        elif event_reject.key == pygame.K_SPACE and player.alive:
                            player.jump = True
                    elif event_reject.type == pygame.KEYUP:
                        if event_reject.key == pygame.K_a:
                            moving_left = False
                        elif event_reject.key == pygame.K_d:
                            moving_right = False
                        elif event_reject.key == pygame.K_SPACE:
                            player.jump = False
                player.move(moving_left, moving_right)
                if stop_run:
                    break
                clock.tick(fps)
            continue
        else:
            launcher()