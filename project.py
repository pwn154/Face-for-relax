import cv2
import time
import easygui
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
last_time = time.time()
elapse = 0
cap = cv2.VideoCapture(0) # 0 = internal webcam, -1 = external webcam
width, height = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

gui = Tk()
gui.wm_title('Face For Relax')
#gui.configure(background='#ffffff')
mlabel = Label(text="Face For Relax", fg="#FFFF00", bg='#000000').pack()
lmain = Label(gui)
lmain.pack()
startstop_frame = Frame(gui)
startstop_frame.pack(pady=10)
aboutus_frame = Frame(gui)
aboutus_frame.pack(side=BOTTOM, pady=10)

def draw_boundary(img, classifier, scaleFactor, minNeightbors, color, text): #color(BGR) >> Blue Green Red
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #แปลงภาพสีเป็นภาพขาวดำ
    features = classifier.detectMultiScale(gray, scaleFactor, minNeightbors)
    coordinate = []
    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2) #(img, top-left corner, bot-right corner, color_border, thickness)
        cv2.putText(img, text, (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        coordinate = [x,y,w,h]
    return img, coordinate

def detect(img, faceCascade):
    img, coordinate = draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face")
    return img, coordinate

def show_frame():
    ret, frame = cap.read()
    frame, coordinate = detect(frame, faceCascade)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    imgtk = ImageTk.PhotoImage(image = Image.fromarray(cv2image))
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, show_frame)

def popup_showinfo():
    messagebox.showinfo(title='Group Member', message=
'62070021 Kanasin Amoornkittisarn\n\
62070090 Tatchaphon Sriargardkraisang\n\
62070113 Prathan Nawieng\n\
62070147 Pattarapol Ngaorattanaphanthikun\n\
62070154 Puwanut Janmee')

# while True:
#     ret, frame = cap.read() # อ่านภาพจากกล้องมาทีละ frame, 1 loop = 1 frame
#     frame, coordinate = detect(frame, faceCascade)
#     cv2.imshow('frame', frame) #แสดง frame
#     if (cv2.waitKey(100) & 0xFF == 27): #27 = esc  >>> ปิดหน้าต่าง
#         break
#     if elapse <= 20:
#         if coordinate != []:
#             elapse = time.time() - last_time #ระบุเวลาที่ผ่านไป
#             print(elapse)
#         else:
#             last_time = time.time() - elapse
#     else:
#         print('Rest your eye!')
#         value = easygui.ynbox('Rest your eye!', 'Face for relax',('yes','no')) #ตัวเลือก
#         if value == False:
#             break
#         else:
#             time.sleep(2) #ระยะเวลาการพัก
#         elapse = 0
#         last_time = time.time()

show_frame()

ButtonStart = Button(startstop_frame, text='Start', command=gui.destroy).pack(side=LEFT, padx=20)
ButtonStop = Button(startstop_frame, text='Stop', command=gui.destroy).pack(side=LEFT, padx=20)
ButtonAbout = Button(aboutus_frame, text='About', command=popup_showinfo).pack(side=BOTTOM)

gui.mainloop()
