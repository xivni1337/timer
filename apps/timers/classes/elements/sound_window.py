import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import shutil
import sqlite3

class SoundWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.folder_img = None
        self.name = tk.StringVar()
        self.path = tk.StringVar()
        self.title('Добавить мелодию:')
        self.geometry('350x150')
        self.grab_set()
        self.protocol(name='WM_DELETE_WINDOW', func=self.dismiss)
        self.resizable(False, False)
        self.fill_window()
        self.DEFAULT_SOUND_PATH = 'static/sounds/'

    def dismiss(self):
        self.grab_release()
        self.destroy()

    def fill_window(self):
        self.name_window_frame = tk.Frame(master=self)
        self.name_window_frame.pack(fill=tk.X, side=tk.TOP)
        self.name_window_label = tk.Label(master=self.name_window_frame, text='Имя', font=('Helvetica bold', 15))
        self.name_window_label.pack(side=tk.LEFT)
        self.name_window_entry = tk.Entry(master=self.name_window_frame, textvariable=self.name)
        self.name_window_entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)

        self.sound_window_frame = tk.Frame(master=self)
        self.sound_window_frame.pack(fill=tk.X, side=tk.TOP)
        self.sound_label = tk.Label(master=self.sound_window_frame, text='Мелодия', font=('Helvetica bold', 15))
        self.sound_label.pack(side=tk.LEFT)
        self.sound_window_entry = tk.Entry(master=self.sound_window_frame, textvariable=self.path)
        self.sound_window_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.folder_img = tk.PhotoImage(file='static/icons/folder.png')
        self.sound_window_button = tk.Button(master=self.sound_window_frame, image=self.folder_img, command=self.choice_sound)
        self.sound_window_button.pack(side=tk.RIGHT)

        self.button_window_frame = tk.Frame(master=self)
        self.button_window_frame.pack()
        self.add_button = tk.Button(master=self.button_window_frame, text='неДобавить', command=self.create_sound)
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.cancel_button = tk.Button(master=self.button_window_frame, text='Отмена')
        self.cancel_button.pack(side=tk.RIGHT, padx=5)

    def choice_sound(self):
        path = tkinter.filedialog.askopenfilename(title='Выбирете мелодию', filetypes=[('Аудио', '.мр3 mpeg .wav')])
        self.path.set(path)

    def create_sound(self):
        name = self.name.get()
        path = self.path.get()
        if not (name and path):
            return
        name_with_ext = name + '.' + path.split('.')[-1]
        try:
            shutil.copyfile(path,self.DEFAULT_SOUND_PATH + name_with_ext)
        except Exception as e:
            print(e)
        conn = sqlite3.connect('timers.db')
        c = conn.cursor()
        c.execute(f'''INSERT INTO sounds (name, path) 
                  values ('{name}','{path}')''')
        conn.commit()
        conn.close()
        self.dismiss()