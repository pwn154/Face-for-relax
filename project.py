import cv2
import time
import easygui

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

def draw_boundary(img, classifier, scaleFactor, minNeightbors, color, text): #color(BGR) >> Blue Green Red
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #แปลงภาพสีเป็นภาพขาวดำ
    features = classifier.detectMultiScale(gray, scaleFactor, minNeightbors)
    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2) #(img, top-left corner, bot-right corner, color_border, thickness)
        cv2.putText(img, text, (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img

def detect(img, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face")
    img = draw_boundary(img, eyeCascade, 1.1, 12, (255,0,0), "Eye")
    return img

cap = cv2.VideoCapture(0) # 0 = internal webcam, -1 = external webcam

while True:
    if elapse <= 10:
        elapse = time.time() - last_time #ระบุเวลาที่ผ่านไป
        print(elapse)
        ret, frame = cap.read() # อ่านภาพจากกล้องมาทีละ frame, 1 loop = 1 frame
        frame = detect(frame, faceCascade)
        cv2.imshow('frame', frame) #แสดง frame
        else:
            print('Rest your eye!')
        value = easygui.ynbox('Rest your eye!', 'Face for relax',('yes','no')) #ตัวเลือก
        if value == False:
            break
        else:
            time.sleep(5) #ระยะเวลาการพัก
        elapse = 0
        last_time = time.time()
cap.release()
cv2.destroyAllWindows()