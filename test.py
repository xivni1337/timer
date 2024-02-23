import tkinter as tk
import datetime


def timer():
    lab.config(text=datetime.datetime.now().strftime('%H:%M:%S'))
    root.after(1000, timer)


root = tk.Tk()

lab = tk.Label(root, font=('Helvetica bold', 24))
lab.pack()

timer()
root.mainloop()
