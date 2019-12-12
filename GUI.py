from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
gui = Tk()
gui.wm_title('Face For Relax')
gui.geometry('650x600')#ขนาดGUI
gui.configure(background='#000000')
mlabel=Label(text="Face For Relax",fg="#FFFF00", bg='#000000').pack()
lmain = Label(gui)
lmain.pack()
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, show_frame)
def popup_showinfo():
    showinfo('My Group', 'Kanasin Amoornkittisarn 62070021\nTatchaphon Sriargardkraisang 62070090\nPrathan Nawieng 62070113\nPattarapol Ngaorattanaphanthikun 62070147\nPuwanut Janmee 62070154')
class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        
        self.button_showinfo = Button(self, text="Start", command=gui.destroy)
        self.button_showinfo.pack()
        
        self.button_showinfo = Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()

app = Application(gui)
show_frame()
gui.mainloop()
