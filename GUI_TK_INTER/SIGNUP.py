from tkinter import *
from tkinter.ttk import *
from functools import partial
def signuping():
    signup= Tk()
    signup.title('Tkinter Login Form - pythonexamples.org')
    signup.geometry('800x800')  
    Label(signup,text="here tou can make a new account").grid(row = 0 ,column = 0)
    signup.mainloop()