import cv2
import time
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
last_time = time.time()
timecounter = 0
state = 0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0 = internal webcam, -1 = external webcam
width, height = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

mixer.init()

gui = Tk()
gui.title('Face For Relax')
gui.option_add("*Font", "TkDefaultFont 16")

lmain = Label(gui)
lmain.grid(row=0, columnspan=2, padx=5, pady=5)

timelabel = Label(gui, text=timecounter, font=("TkDefaultFont", 30))
timelabel.grid(row=1, columnspan=2, pady=5)

timeset_frame = Frame(gui)
timeset_frame.grid(row=2, columnspan=2, pady=10)
time_text = Label(timeset_frame, text="Time Settings: ").pack(side=LEFT)

set_hour = ttk.Combobox(timeset_frame, values=list(range(24)), width=3, state="readonly")
set_hour.current(0)
set_hour.pack(side=LEFT, padx=5)
hour_text = Label(timeset_frame, text="hr.").pack(side=LEFT)

set_minute = ttk.Combobox(timeset_frame, values=list(range(60)), width=3, state="readonly")
set_minute.current(0)
set_minute.pack(side=LEFT, padx=5)
minute_text = Label(timeset_frame, text="min.").pack(side=LEFT)

set_second = ttk.Combobox(timeset_frame, values=list(range(60)), width=3, state="readonly")
set_second.current(0)
set_second.pack(side=LEFT, padx=5)
second_text = Label(timeset_frame, text="s.").pack(side=LEFT)

def draw_boundary(img, classifier, scaleFactor, minNeightbors, color, text): #color(BGR) >> Blue Green Red
    """วาดกรอบสี่เหลี่ยมเพื่อเป็นบล๊อคสำหรับตรวจจับใบหน้า"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #แปลงภาพสีเป็นภาพขาวดำ
    features = classifier.detectMultiScale(gray, scaleFactor, minNeightbors)
    coordinate = []
    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2) #(img, top-left corner, bot-right corner, color_border, thickness)
        cv2.putText(img, text, (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        coordinate = [x,y,w,h]
    return img, coordinate

def detect(img, faceCascade):
    """การตวจจับใบหน้า"""
    img, coordinate = draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face")
    return img, coordinate

def popup_showinfo():
    """แสดงข้อมูลรายชื่อสมาชิกของกลุ่ม"""
    messagebox.showinfo(title='Group Member', message=
'62070021 Kanasin Amornkittisarn\n\
62070090 Tatchaphon Sriargardkraisang\n\
62070113 Prathan Nawieng\n\
62070147 Pattarapol Ngaorattanaphanthikun\n\
62070154 Puwanut Janmee')

def show_frame():
    """show each frame and count time when in start state"""
    global timecounter, last_time
    timerelax = int(set_hour.get())*3600 + int(set_minute.get())*60 + int(set_second.get())
    ret, frame = cap.read()
    if state == 1:#state Start
        frame, coordinate = detect(frame, faceCascade)
        if timecounter <= timerelax:
            if coordinate != []:
                timecounter = time.time() - last_time #ระบุเวลาที่ผ่านไป
            else:
                last_time = time.time() - timecounter
        else:
            mixer.music.load('Success_ding_sound.mp3')
            mixer.music.play()
            value = messagebox.askyesno(title='Face for relax', message='Are you going to rest?') #ตัวเลือก
            if value == True:
                change_state(0)
            else:
                time.sleep(2) #ระยะเวลาการพักก่อนที่เริ่ม detect หน้าอีกครั้ง
                timecounter = 0
                last_time = time.time()
    else:#state Reset
        timecounter = 0
        last_time = time.time()

    timeformat = str(datetime.timedelta(seconds=int(timecounter)))
    timelabel.configure(text="Timer: %s"%timeformat)

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    imgtk = ImageTk.PhotoImage(image = Image.fromarray(cv2image))
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

    # delay = time (milliseconds)
    if state == 1:
        delay = 100 #สามารถลด Delay ลงได้ แต่จะทำให้เกิดการประมวลผลถี่เกินความจำเป็น
    else:
        delay = 10
    lmain.after(delay, show_frame)

def change_state(value):
    global state
    state = value

show_frame()

ButtonStart = Button(gui, width=20, bg='lightgreen', text='Start', command=lambda *args: change_state(1))
ButtonStart.grid(row=3, column=0, sticky=E, padx=5)#ปุ่มกดจับเวลา

ButtonReset = Button(gui, width=20, bg='red', text='Reset', command=lambda *args: change_state(0))
ButtonReset.grid(row=3, column=1, sticky=W, padx=5)#ปุ่มหยุดโปรแกรม

ButtonAbout = Button(gui, text='About us', command=popup_showinfo)
ButtonAbout.grid(row=4, columnspan=2, pady=10)#ปุ่มแสดงข้อมูลรายชื่อ

gui.mainloop()
