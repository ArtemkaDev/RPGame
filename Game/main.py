from tkinter import Canvas, Tk, StringVar, PhotoImage, Button, Entry
from modules.player import Solider
from modules.jsons import jsons
from threading import Thread
import webbrowser
import modloader
import pygame
import json
import time
import sys
import os

# value
test_mod = True
in_game = False
auth = False
fps_now = ""
moving_left = False
moving_right = False

# json
jsons().check()
with open(os.path.expanduser(f"{os.getenv('APPDATA')}/ProjectRedAdventure/config.json"), "r") as json_file:
    config_json = json.load(json_file)

# launcher
tkinter = Tk()
name = StringVar()
password = StringVar()


def btn_clicked():
    global auth
    auth = True
    tkinter.destroy()


def openwebreg():
    webbrowser.open("https://projectredcite.herokuapp.com/reg")


tkinter.title('ProjectRed Adventure Launcher')
tkinter.geometry("600x350")
tkinter.configure(bg="#ffffff")
canvas = Canvas(tkinter, bg="#ffffff", height=350, width=600, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"./img/Launcher/enter/background.png")
background = canvas.create_image(300.0, 175.0, image=background_img)

img0 = PhotoImage(file=f"./img/Launcher/enter/img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=openwebreg, relief="flat")
b0.place(x=436, y=314, width=156, height=25)

img1 = PhotoImage(file=f"./img/Launcher/enter/img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b1.place(x=341, y=235, width=156, height=25)

# entry 0
entry0_img = PhotoImage(file=f"./img/Launcher/enter/img_textBox0.png")
entry0_bg = canvas.create_image(418.5, 139.5, image=entry0_img)
entry0 = Entry(bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=name)
entry0.place(x=340.0, y=127, width=157.0, height=23)

# entry 1
entry1_img = PhotoImage(file=f"./img/Launcher/enter/img_textBox1.png")
entry1_bg = canvas.create_image(418.5, 203.5, image=entry1_img)
entry1 = Entry(bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=password)
entry1.place(x=340.0, y=191, width=157.0, height=23)

tkinter.resizable(False, False)
tkinter.mainloop()


# end


# stop
def stop():
    pygame.quit()
    sys.exit()


# game
pygame.init()
base_font = pygame.font.SysFont("Futura", 48)


# screen stats
def screen_init():
    global screen, proc_x, proc_y
    if config_json['screen']['mode'] == 1 and auth:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF, 16)
        proc_x = pygame.display.get_surface().get_size()[0] / 300
        proc_y = pygame.display.get_surface().get_size()[1] / 200
    elif config_json['screen']['mode'] == 2 and auth:
        screen = pygame.display.set_mode((config_json['screen']['width'], config_json['screen']['height']))
        proc_x = pygame.display.get_surface().get_size()[0] / 300
        proc_y = pygame.display.get_surface().get_size()[1] / 200


screen_init()

pygame.display.set_caption('ProjectRed Adventures')
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# fps
clock = pygame.time.Clock()
fps = config_json['fps']

# create player
player = Solider("default", 30, 152, 20, 40, 10, screen, proc_x, proc_y)



# background
def draw_bg():
    screen.fill((144, 201, 120))
    pygame.draw.line(screen, pygame.Color("red"), (10 * proc_x, 180 * proc_y), (300 * proc_x, 180 * proc_y), width=3)


# mod
modloader.mod(test_mod).start()
modloader.mod(test_mod).load()

# input
user_text = ''


# tick
def tick_start():
    global fps_now, in_game
    sleep = 0.02
    time.sleep(0.5)
    if clock.get_fps() <= 30:
        sleep = 0.1
    while True:
        if not in_game:
            break
        fps_now = str(int(clock.get_fps()))
        if player.alive:
            if moving_left or moving_right:
                player.update_action(1)  # run
            else:
                player.update_action(0)  # stay
        time.sleep(sleep)


def main_start():
    global in_game, fps
    Thread(target=tick_start).start()
    in_game = True
    while True:
        # draw
        draw_bg()
        player.update_animation()
        player.draw()
        screen.blit(base_font.render(fps_now, True, pygame.Color("white")), (10, 10))
        # event
        for event_reject in pygame.event.get():
            if event_reject.type == pygame.QUIT:
                in_game = False
                stop()
            elif event_reject.type == pygame.KEYDOWN:
                if event_reject.key == pygame.K_ESCAPE:
                    in_game = False
                    stop()
                elif event_reject.key == pygame.K_a:
                    player.moving_left = True
                elif event_reject.key == pygame.K_d:
                    player.moving_right = True
                elif event_reject.key == pygame.K_SPACE and player.alive:
                    player.jump = True
            elif event_reject.type == pygame.KEYUP:
                if event_reject.key == pygame.K_a:
                    player.moving_left = False
                elif event_reject.key == pygame.K_d:
                    player.moving_right = False
                elif event_reject.key == pygame.K_SPACE:
                    player.jump = False
        player.move()
        pygame.display.update()  # update
        clock.tick(fps)


# run
if __name__ == '__main__':
    if not auth:
        stop()
    elif auth:
        main_start()