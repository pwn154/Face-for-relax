import cv2
import time
import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
last_time = time.time()
timecounter = 0
state = 0

cap = cv2.VideoCapture(0) # 0 = internal webcam, -1 = external webcam
width, height = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

mixer.init()

gui = Tk()
gui.title('Face For Relax')
#gui.configure(background='#ffffff')
mlabel = Label(text="Face For Relax", fg="#FFFF00", bg='#000000').pack()

lmain = Label(gui)
lmain.pack()

timelabel = Label(gui, text=timecounter, bg="lightblue", width=20, relief="solid")
timelabel.pack(pady=10)

startstop_frame = Frame(gui)
startstop_frame.pack(pady=5)

aboutus_frame = Frame(gui)
aboutus_frame.pack(side=BOTTOM, pady=5)

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
    ret, frame = cap.read()
    if state == 1:#state Start
        frame, coordinate = detect(frame, faceCascade)
        if timecounter <= 10:
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
    timelabel.configure(text="Time: %s"%timeformat)

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

ButtonStart = Button(startstop_frame, width=20, bg='lightgreen', text='Start', command=lambda *args: change_state(1))
ButtonStart.pack(side=LEFT, padx=20)#ปุ่มกดจับเวลา

ButtonReset = Button(startstop_frame, width=20, bg='red', text='Reset', command=lambda *args: change_state(0))
ButtonReset.pack(side=LEFT, padx=20)#ปุ่มหยุดโปรแกรม

ButtonAbout = Button(aboutus_frame, text='About us', command=popup_showinfo)
ButtonAbout.pack()#ปุ่มแสดงข้อมูลรายชื่อ

gui.mainloop()
