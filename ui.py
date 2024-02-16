import tkinter as tk
from main import boot

def power_on_action():
    pass
    
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

startup = tk.Button(widget_bg, text="POWER ON CAMERA")
startup.pack(side="left")

exit = tk.Button(widget_bg, text="EXIT",command=exit_action)
exit.pack(side="left",padx=10)

app.mainloop()