import tkinter as tk

app = tk.Tk()
width = 300
height = 300
left = int(float(app.winfo_screenheight())/2)
top = int(float(app.winfo_width())/2)
app.geometry(f'{width}x{height}+{left}+{top}')
app.winfo_name="OpenCV Minecraft Interface Launcher"


app.mainloop()