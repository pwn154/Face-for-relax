from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

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
    messagebox.showinfo('Group Member',
'62070021 Kanasin Amoornkittisarn\n\
62070090 Tatchaphon Sriargardkraisang\n\
62070113 Prathan Nawieng\n\
62070147 Pattarapol Ngaorattanaphanthikun\n\
62070154 Puwanut Janmee')

show_frame()

ButtonStart = Button(startstop_frame, width=20, bg='lightgreen', text='Start', command=gui.destroy)#ตั้งเป็น gui.detroy เพราะยังไม่ได้รวมกับฟงัชั่นอื่นๆ
ButtonStart.pack(side=LEFT, padx=20)#ปุ่มกดจับเวลา

ButtonReset = Button(startstop_frame, width=20, bg='red', text='Reset', command=gui.destroy)
ButtonReset.pack(side=LEFT, padx=20)#ปุ่มหยุดโปรแกรม

ButtonAbout = Button(aboutus_frame, text='About us', command=popup_showinfo)
ButtonAbout.pack()#ปุ่มแสดงข้อมูลรายชื่อ
gui.mainloop()
