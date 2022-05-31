import tkinter as tks
from tkinter import filedialog as fd
import menu as n
import os
from Background_Removal import bgRemoval
from Background_Blurring import bgBlurring
from Background_Grayscale import bgGrayscale
from Background_Change import bgChange
import cv2

dir = str(os.getcwd())
dir = dir + '\\images'


class Start(tks.Tk):
    def __init__(self):
        super().__init__()
        self.image = None
        self.tmp = dir + '/tmp.png'
        if os.path.exists(self.tmp):
            os.remove(self.tmp)
        self.geometry("1280x720+100+50")
        self.configure(bg="#ffffff")
        canvas = tks.Canvas(
            self,
            bg="#ffffff",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = tks.PhotoImage(file=dir + "/backgroundS.png")
        canvas.create_image(
            558.5, 395.0,
            image=background_img)

        icon = tks.PhotoImage(file=dir + "/icon.png")
        self.iconphoto(False, icon)

        imgOriginal = tks.PhotoImage(None)
        self.bO = tks.Label(
            image=imgOriginal,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.bO.place(
            x=108, y=135,
            width=450,
            height=450)

        imgResult = tks.PhotoImage(None)
        self.bR = tks.Button(
            image=imgResult,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.bR.place(
            x=739, y=135,
            width=450,
            height=450)

        img3 = tks.PhotoImage(file=dir + "/img3.png")
        self.b3 = tks.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_rotate_right,
            relief="flat")

        self.b3.place(
            x=1015, y=78,
            width=50,
            height=50)

        img4 = tks.PhotoImage(file=dir + "/img4.png")
        self.b4 = tks.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_flip_ver,
            relief="flat")

        self.b4.place(
            x=1139, y=78,
            width=50,
            height=50)

        img5 = tks.PhotoImage(file=dir + "/img5.png")
        self.b5 = tks.Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_flip_hor,
            relief="flat")

        self.b5.place(
            x=1077, y=78,
            width=50,
            height=50)

        img6 = tks.PhotoImage(file=dir + "/img6.png")
        b6 = tks.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_reset,
            relief="flat")

        b6.place(
            x=446, y=78,
            width=50,
            height=50)

        img7 = tks.PhotoImage(file=dir + "/img7.png")
        self.b7 = tks.Button(
            image=img7,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_saveFile,
            relief="flat")

        self.b7.place(
            x=384, y=77,
            width=50,
            height=50)

        img8 = tks.PhotoImage(file=dir + "/img8.png")
        self.b8 = tks.Button(
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_newFile,
            relief="flat")

        self.b8.place(
            x=322, y=78,
            width=50,
            height=50)

        img9 = tks.PhotoImage(file=dir + "/img9.png")
        self.b9 = tks.Button(
            image=img9,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_back,
            relief="flat")

        self.b9.place(
            x=508, y=78,
            width=50,
            height=50)

        img10 = tks.PhotoImage(file=dir + "/img10.png")
        self.b10 = tks.Button(
            image=img10,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_rotate_left,
            relief="flat")

        self.b10.place(
            x=953, y=78,
            width=50,
            height=50)

        img11 = tks.PhotoImage(file=dir + "/img11.png")
        self.b11 = tks.Button(
            image=img11,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_remove,
            relief="flat")

        self.b11.place(
            x=64, y=651,
            width=199,
            height=51)

        img12 = tks.PhotoImage(file=dir + "/img12.png")
        self.b12 = tks.Button(
            image=img12,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_greyscale,
            relief="flat")

        self.b12.place(
            x=1009, y=651,
            width=199,
            height=51)

        img13 = tks.PhotoImage(file=dir + "/img13.png")
        self.b13 = tks.Button(
            image=img13,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_change,
            relief="flat")

        self.b13.place(
            x=379, y=651,
            width=199,
            height=51)

        img14 = tks.PhotoImage(file=dir + "/img14.png")
        self.b14 = tks.Button(
            image=img14,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_blur,
            relief="flat")

        self.b14.place(
            x=694, y=651,
            width=199,
            height=51)

        self.title("Foreground - Background Separator")
        self.resizable(False, False)
        self.mainloop()

    def btn_newFile(self):
        file = fd.askopenfilename(initialdir=dir, title="Select Image File",
                                  filetypes=(("PNG File", "*.png"),
                                             ("JPG File", "*.jpg"), ("All File", "*.*")))
        self.image = file
        temp = cv2.imread(self.image)
        cv2.imwrite(os.path.join(dir, 'tmp.png'), temp)
        img = tks.PhotoImage(file=file)
        self.bO.configure(image=img)
        self.bO.image = img
        self.bR.configure(image=img)
        self.bR.image = img

    def btn_saveFile(self):
        save = fd.asksaveasfilename(defaultextension='.png', initialdir=dir, title="Save File As",
                                    filetypes=(("PNG File", ".png"),
                                               ("JPG File", ".jpg"),
                                               ("All File", ".*")))
        saveArray = save.split('/')
        name = saveArray[len(saveArray) - 1]
        path = save.replace(name, '')
        img = cv2.imread(self.tmp)
        cv2.imwrite(os.path.join(path, name), img)

    def btn_reset(self):
        img = cv2.imread(self.image)
        cv2.imwrite(os.path.join(dir, 'tmp.png'), img)
        imgR = tks.PhotoImage(file=self.tmp)
        self.bR.configure(image=imgR)
        self.bR.image = imgR

    def btn_back(self):
        self.destroy()
        n.Menu()

    def btn_remove(self):
        self.showWait(1)
        result = bgRemoval(self.tmp)
        result = cv2.convertScaleAbs(result, alpha=255.0)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        resized = resize_image(result)
        img = getResult(resized)
        self.bR.configure(image=img)
        self.bR.image = img
        self.showWait(0)

    def btn_change(self):
        self.showWait(1)
        file = fd.askopenfilename(initialdir=dir, title="Select Image File",
                                  filetypes=(("PNG File", "*.png"),
                                             ("JPG File", "*.jpg"), ("All File", "*.*")))
        result = bgChange(self.tmp, file)
        result = cv2.convertScaleAbs(result, alpha=255.0)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        resized = resize_image(result)
        img = getResult(resized)
        self.bR.configure(image=img)
        self.bR.image = img
        self.showWait(0)

    def btn_blur(self):
        self.showWait(1)
        result = bgBlurring(self.tmp)
        result = cv2.convertScaleAbs(result, alpha=255.0)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        resized = resize_image(result)
        img = getResult(resized)
        self.bR.configure(image=img)
        self.bR.image = img
        self.showWait(0)

    def btn_greyscale(self):
        self.showWait(1)
        result = bgGrayscale(self.tmp)
        result = cv2.convertScaleAbs(result, alpha=255.0)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        resized = resize_image(result)
        img = getResult(resized)
        self.bR.configure(image=img)
        self.bR.image = img
        self.showWait(0)

    def btn_rotate_right(self):
        tmp = cv2.imread(self.tmp)
        tmp = cv2.rotate(tmp, cv2.cv2.ROTATE_90_CLOCKWISE)
        img = getResult(tmp)
        self.bR.configure(image=img)
        self.bR.image = img

    def btn_rotate_left(self):
        tmp = cv2.imread(self.tmp)
        tmp = cv2.rotate(tmp, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        img = getResult(tmp)
        self.bR.configure(image=img)
        self.bR.image = img

    def btn_flip_hor(self):
        tmp = cv2.imread(self.tmp)
        tmp = cv2.flip(tmp, 1)
        img = getResult(tmp)
        self.bR.configure(image=img)
        self.bR.image = img

    def btn_flip_ver(self):
        tmp = cv2.imread(self.tmp)
        tmp = cv2.flip(tmp, 0)
        img = getResult(tmp)
        self.bR.configure(image=img)
        self.bR.image = img

    def showWait(self, ck):
        if ck == 1:
            self.title('Please wait...')
        else:
            self.title("Foreground - Background Separator")


def getResult(img):
    cv2.imwrite(os.path.join(dir, 'tmp.png'), img)
    result = tks.PhotoImage(file=dir + "/tmp.png")
    return result


def resize_image(image):
    if image.shape[1] > image.shape[0]:
        width = 450
        height = int(image.shape[0] * 450 / image.shape[1])
    elif image.shape[1] < image.shape[0]:
        height = 450
        width = int(image.shape[1] * 450 / image.shape[0])
    else:
        width = 450
        height = 450
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized
