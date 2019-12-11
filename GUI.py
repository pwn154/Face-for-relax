from tkinter import *
import cv2
from PIL import Image, ImageTk
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
def detect(img, faceCascade):
    img, coordinate = draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face")
    return img, coordinate
def popup_bonus():
    win = Toplevel()
    win.wm_title("About us")
    l1 = Label(win, text="Kanasin Aonrkittisarn")
Button1 = Button(text='Start', command=gui.destroy).pack()#ยังไม่ได้แก้ Command
Button2 = Button(text='About', command=popup_bonus).pack()#กะจะใส่ฟังก์ชั่นรายชื่อ Command
show_frame()
gui.mainloop()
