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
        value = easygui.ynbox('Rest your eye!', 'Face for relax',('yes','no'))
        if value == False:
            break
        else:
            time.sleep(5)
        elapse = 0
        last_time = time.time()
