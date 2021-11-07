from tkinter import *


class launcher(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x350')
        self.configure(bg="#ffffff")
        self.title('ProjectRed Adventure Launcher')
        self.name = StringVar(self).get()
        self.password = StringVar(self).get()
        self.canvas = Canvas(self, bg="#ffffff", height=350, width=600, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file="./img/Launcher/enter/background.png")
        self.background = self.canvas.create_image(300.0, 175.0, image=self.background_img)
        self.img0 = PhotoImage(file="./img/Launcher/enter/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat")
        self.b0.place(x=341, y=235, width=156, height=25)
        self.entry0_img = PhotoImage(file="./img/Launcher/enter/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(418.5, 139.5, image=self.entry0_img)
        self.entry0 = Entry(bd=0, textvariable=self.name, bg="#c4c4c4", highlightthickness=0)
        self.entry0.place(x=340.0, y=127, width=157.0, height=23)
        self.entry1_img = PhotoImage(file="./img/Launcher/enter/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(418.5, 203.5, image=self.entry1_img)
        self.entry1 = Entry(bd=0, textvariable=self.password, bg="#c4c4c4", highlightthickness=0)
        self.entry1.place(x=340.0, y=191, width=157.0, height=23)
        self.resizable(False, False)
        self.mainloop()

    def btn_clicked(self):
        print("lol", self.name)