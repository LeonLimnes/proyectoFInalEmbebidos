#!/usr/bin/env python3
import os
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import Text
from tkinter.messagebox import showinfo

def getRoms():
    path = "/home/pi/Desktop/proyectoFInalEmbebidos/ROMS/GBC"
    dir_list = os.listdir(path)
    return dir_list


# create the root window
def guiListRoms():
    root = tk.Tk()
    root.resizable(False, False)
    root.title('Lista ROMS')

    window_height = 200
    window_width = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)


    # create a list box
    langs = getRoms()

    langs_var = tk.StringVar(value=langs)

    listbox = tk.Listbox(
        root,
        listvariable=langs_var,
        height=6)

    listbox.grid(
        column=0,
        row=0,
        sticky='nwes'
    )

    # link a scrollbar to a list
    scrollbar = ttk.Scrollbar(
        root,
        orient='vertical',
        command=listbox.yview
    )

    listbox['yscrollcommand'] = scrollbar.set

    scrollbar.grid(
        column=1,
        row=0,
        sticky='ns')
    
    #root.after(3000,lambda:root.destroy())
    root.lift()
    root.attributes('-topmost',True)
    root.mainloop()
