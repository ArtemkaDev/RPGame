from tkinter import *
import webbrowser, os


auth = False
window = Tk()
name = StringVar()
password = StringVar()


def btn_clicked():
    global auth
    while True:
        if auth:
            window.destroy()
            os.startfile(".\main.exe")
            break
        elif not auth:
            auth = True
            continue


def openreg():
    webbrowser.open("https://projectredcite.herokuapp.com/reg")


window.title('ProjectRed Adventure Launcher')
window.geometry("600x350")
window.configure(bg="#ffffff")
canvas = Canvas(window, bg="#ffffff", height=350, width=600, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file = f"./img/Launcher/enter/background.png")
background = canvas.create_image(300.0, 175.0, image=background_img)

img0 = PhotoImage(file = f"./img/Launcher/enter/img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=openreg, relief="flat")
b0.place(x=436, y=314, width=156, height=25)

img1 = PhotoImage(file = f"./img/Launcher/enter/img1.png")
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

window.resizable(False, False)
window.mainloop()
