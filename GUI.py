from tkinter import *
import cv2
from PIL import Image, ImageTk

gui = Tk()
gui.geometry('650x600')#ขนาดGUI
mlabel=Label(text="Face For Relax",fg="#FFFF00",bg="black").pack()
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

show_frame()
bottom1 = Button(gui, text='Start', width=25, commnand=gui.destroy).pack()
button2 = Button(gui, text='Stop', width=25, command=gui.destroy).pack()
gui.mainloop()
