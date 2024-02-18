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

def update_output(output_text, process):
    for line in iter(process.stdout.readline, b''):
        output_text.insert("end", line)
        output_text.see("end")
    process.stdout.close()

def power_on_action():
    output_window = tk.Toplevel(app)
    output_window.title("Output Log")
    output_text = tk.Text(output_window)
    output_text.pack(expand=True, fill="both")
    global process
    process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output_thread = threading.Thread(target=update_output, args=(output_text, process), daemon=True)
    output_thread.start()

    
    
def exit_action():
    process.kill()
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

exit = tk.Button(app, text="EXIT",command=exit_action)
exit.pack()


environment['text']="Environment: READY !"
if not test_env():
    environment['text']="Environment: NOT READY !"
    environment
    messagebox.showerror(title="Notice",message="Environment: NOT READY !")

app.mainloop()