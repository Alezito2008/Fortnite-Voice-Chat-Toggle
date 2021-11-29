import tkinter
from tkinter import *
import time
import threading
import pyautogui
import keyboard
app=tkinter.Tk()
app.wm_attributes('-transparentcolor', 'black')
app.wm_attributes('-topmost', True)
app.overrideredirect(True)
app.config(bg='black')
app.geometry('1920x1080')
toggle = 0
statustext=StringVar()
statuslbl = Label(app, textvariable=statustext, font='Arial 20 bold', bg='black')
statuslbl.place(x=15, y=15)
def keydetect():
    global toggle
    while True:
        if keyboard.is_pressed('f1'):
            toggle = toggle + 1
            if toggle == 2:
                toggle = 0
            time.sleep(0.2)
        if keyboard.is_pressed('alt'):
            toggle = 0
def textchange():
    global toggle
    global statustext
    while True:
        time.sleep(0.1)
        if toggle==0:
            statustext.set('Disabled')
            statuslbl.config(fg='red')
            pyautogui.keyUp('f1')
        if toggle==1:
            statustext.set('Enabled')
            statuslbl.config(fg='lime')
            pyautogui.keyDown('f1')
threading.Thread(target=keydetect).start()
threading.Thread(target=textchange).start()

app.mainloop()