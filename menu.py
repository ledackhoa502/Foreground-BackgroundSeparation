import tkinter as tk
from tkinter import messagebox
from start import Start
import os

dir = str(os.getcwd())
dir = dir + '\\images'


def btn_info():
    messagebox.showinfo('Info', 'Author: Tran Quang Sang, Le Dac Khoa\nEmail: tqsang.19it5@vku.udn.vn')


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720+100+50")
        self.configure(bg="#ffffff")
        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        icon = tk.PhotoImage(file=dir + "/icon.png")
        self.iconphoto(False, icon)

        img0 = tk.PhotoImage(file=dir + "/img0.png")
        b0 = tk.Button(
            bg='#ffffff',
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_info,
            relief="flat")

        b0.place(
            x=809, y=397,
            width=150,
            height=150)

        img1 = tk.PhotoImage(file=dir + "/img1.png")
        b1 = tk.Button(
            bg='#ffffff',
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_exit,
            relief="flat")

        b1.place(
            x=994, y=347,
            width=100,
            height=100)

        img2 = tk.PhotoImage(file=dir + "/img2.png")
        b2 = tk.Button(
            bg='#ffffff',
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_start,
            relief="flat")

        b2.place(
            x=515, y=272,
            width=250,
            height=250)

        background_img = tk.PhotoImage(file=dir + "/background.png")
        canvas.create_image(
            768.0, 377.5,
            image=background_img)

        self.title("Foreground - Background Separator")
        self.resizable(False, False)
        self.mainloop()

    def btn_start(self):
        self.destroy()
        Start()

    def btn_exit(self):
        self.destroy()
