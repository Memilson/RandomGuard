# -*- coding: utf-8 -*-
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.master = master
        self.init_widgets()

    def init_widgets(self):
        self.label = Label(self.master, text="Olá, Tkinter!")
        self.label.pack()

root = Tk()
root.title("Minha Aplicação Tkinter")
app = Application(root)
root.mainloop()
