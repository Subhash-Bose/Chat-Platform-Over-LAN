from tkinter import *
from functools import partial



tkWindow = Tk()  
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	qwe=username.get().upper()
	if(qwe=="ROHIT" and password.get()=="123"):
			tkWindow.destroy()
			tkWindow2 = Tk()
			tkWindow2.title('Tkinter Login Form - pythonexamples.org')
			tkWindow2.geometry('800x800')  
			Label(tkWindow2,text="WelcomE").grid(row = 0 ,column = 0)
			tkWindow2.mainloop()
	else:
			tkWindow.destroy()
			tkWindow2 = Tk()
			tkWindow2.geometry('800x800')
			tkWindow2.title('Tkinter Login Form - pythonexamples.org')
			Label(tkWindow2,text="Invalid username or password",font=("Helvetica", "16") ).grid(row = 0 ,column = 0)
			tkWindow2.mainloop()
		   


	    




     


	
	
	

#window

tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box

usernameLabel = Label(tkWindow, text="User Name",padx=20).place(x=680,y=120)  
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=680,y=140)   

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",padx=20 ).place(x=680,y=160)  
password = StringVar() 
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=680,y=180)   

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).place(x=712,y=200)    
tkWindow.mainloop()
