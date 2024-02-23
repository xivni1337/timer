import tkinter as tk
import datetime
from tkinter import ttk
import sqlite3
from classes.elements.sound_window import SoundWindow


def create_data_bases():
    conn = sqlite3.connect('timers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS timers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT,
                                        sound_id INTEGER,
                                        duration INTEGER,
                                        FOREIGN KEY (sound_id) REFERENCES sounds(id) 
                                        )''')
    c.execute('''CREATE TABLE IF NOT EXISTS timers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT
                                        path TEXT
                                        )''')
    conn.commit()
    conn.close()


def crete_timer_record():
    pass


def add_sound():
    sound_window = SoundWindow()


def timer():
    timer_label.config(text=datetime.datetime.now().strftime('%H:%M:%S'))
    root.after(1000, timer)


root = tk.Tk()
root.title('Таймеры')
root.geometry('800x600')

info_frame = tk.Frame(root)
info_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

timer_label = tk.Label(master=info_frame, font=('Helvetica bold', 35))
timer_label.pack(side=tk.TOP)

timers_listbox = tk.Listbox(info_frame)
timers_listbox.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

info_button_frame = tk.Frame(info_frame)
info_button_frame.pack(expand=False, side=tk.TOP)

btn_start = tk.Button(info_button_frame, text='Начать')
btn_start.pack(side=tk.LEFT)

btn_delete = tk.Button(info_button_frame,text='Удалить')
btn_delete.pack(side=tk.RIGHT)

btn_stop = tk.Button(info_button_frame,text='Остановить')
btn_stop.pack()

setting_frame = tk.Frame(root)
setting_frame.pack(expand=True, side=tk.RIGHT, fill=tk.BOTH)

name_frame = tk.Frame(setting_frame)
name_frame.pack(side=tk.TOP, fill=tk.X)
name_label = tk.Label(master=name_frame, text='Имя', font=('Helvetica bold', 15))
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(master=name_frame)
name_entry.pack(side=tk.RIGHT, fill=tk.X,expand=True)

sounds =['Standard', 'super', 'puper']
sound_frame = tk.Frame(setting_frame)
sound_frame.pack(fill=tk.X, side=tk.TOP)
sound_label = tk.Label(master=sound_frame, text='Звук', font=('Helvetica bold', 15))
sound_label.pack(side=tk.LEFT)
sound_combobox = ttk.Combobox(master=sound_frame, values=sounds, state='readonly')
sound_combobox.pack(side=tk.LEFT, fill=tk.X,expand=True)
plus_img = tk.PhotoImage(file='static/icons/plus.png')
add_sound_button = tk.Button(master=sound_frame, image=plus_img,command=add_sound)
add_sound_button.pack(side=tk.RIGHT,ipadx=3,ipady=3)

slider_frame = tk.Frame(setting_frame)
slider_frame.pack(side=tk.TOP, fill=tk.X)
slider_label = tk.Label(master=slider_frame, text='Время', font=('Helvetica bold', 15))
slider_label.pack(side=tk.LEFT)
scale = tk.Scale(master=slider_frame, from_=5, to=180,orient='horizontal')
scale.pack(fill=tk.X, side=tk.RIGHT, expand=True)

create_button_frame = tk.Frame(setting_frame)
create_button_frame.pack(side=tk.TOP)
create_button = tk.Button(master=create_button_frame,text='Создать', command=crete_timer_record)
create_button.pack(side=tk.LEFT)
edit_button = tk.Button(master=create_button_frame,text='Изменять')
edit_button.pack(side=tk.RIGHT)

create_data_bases()
timer()
root.mainloop()
