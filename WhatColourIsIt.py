from tkinter import * 
from tkinter.ttk import *
from time import strftime 
  

root = Tk() 
root.title('What Colour is it?')


def time(): 
    string = strftime('%H:%M:%S') 
    w.config(text = string)
    w.after(1000, time)
    color = strftime('%H%M%S')
    root.configure(bg = '#' + color)
  

w = Label(root, font = ('comic sans ms', 40, 'bold'), 
            background = 'black', 
            foreground = 'white') 
  

w.place(relx = 0.5, rely = 0.5, anchor = 'center') 
root.geometry("500x500")
time() 
  
mainloop() 
