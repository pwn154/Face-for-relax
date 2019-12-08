from tkinter import *
##code
### StarT Gui ###
gui=Tk()
gui.geometry('650x500')
gui.title("Face For Relax")
gui.configure(background='#BDBDBD')
mlabel=Label(text="Face For Relax",fg="#FFFF00",bg="black").pack()
###photo
button = Button(gui, text='Stop', width=25, command=gui.destroy)
button.pack() 
gui.mainloop()


#มีปุ่ม Start Stop
#มีเสียง มี Pop up desktop
