import time
import easygui

last_time = time.time()
elapse = 0
while True:
    if elapse <= 10:
        elapse = time.time() - last_time
        print(elapse)
    else:
        print('Rest your eye!')
        value = easygui.ynbox('พ่อมึงตาย', 'สวัสดี',('yes','no'))
        if value == False:
            break
        elapse = 0
        last_time = time.time()
