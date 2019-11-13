import time
import easygui

last_time = time.time()
elapse = 0
while True:
    if elapse <= 10: #ถ้าน้อยกว่าเท่ากับ 10 หน่วยเป็นวินาที
        elapse = time.time() - last_time #ระบุเวลาที่ผ่านไป
        print(elapse)
    else:
        print('Rest your eye!')
        value = easygui.ynbox('Rest your eye!', 'Face for relax',('yes','no')) #ตัวเลือก
        if value == False:
            break
        else:
            time.sleep(5) #ระยะเวลาการพัก
        elapse = 0
        last_time = time.time()
