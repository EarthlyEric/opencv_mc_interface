import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

def test_env():
    try:
        import cv2
        import mediapipe
        import tkinter
        import pydirectinput
    except:
        return False

    return True

def power_on_action():
    global process
    process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

def stop_action():
    process.kill()   
    
def exit_action():
    app.destroy()

app = tk.Tk()
width = 300
height = 300
left = int(float(app.winfo_screenheight())/2)
top = int(float(app.winfo_width())/2)
app.geometry(f'{width}x{height}+{left}+{top}')

app.title("OpenCV MC Interface")

widget_bg = tk.Frame(app,bg="light gray")
widget_bg.pack(expand=True)

environment= tk.Label(widget_bg,text="Environment: ...")
environment.pack()

poweron = tk.Button(widget_bg, text="POWER ON CAMERA",command=power_on_action)
poweron.pack(side="left")

stop = tk.Button(app, text="STOP",command=stop_action)
stop.pack()

exit = tk.Button(app, text="EXIT",command=exit_action)
exit.pack()

environment['text']="Environment: READY !"
if not test_env():
    environment['text']="Environment: NOT READY !"
    environment
    messagebox.showerror(title="Notice",message="Environment: NOT READY !")

app.mainloop()