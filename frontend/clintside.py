# import all the required modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter.messagebox import showinfo
import regex as re
import smtplib
import socket
import ssl
import threading
import time
from tkinter import *
from tkinter import font
from tkinter import ttk
from login import login
from login import wrong
from signup import signup
from chat import chat
# import all functions /
# everything from chat.py file


PORT = 5000
SERVER = "172.16.181.29"
SERVER = "172.16.185.40"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
client.connect(ADDRESS)

def createSignup():
	print("sign req initiated")
	signup_data=signup()
	print("signup data",signup_data,len(signup_data))
	if(len(signup_data)==1):
		return
	client.send("signup".encode(FORMAT))
	client.send(str(":".join(signup_data)).encode(FORMAT))
	print("sign up requested")
	
	msg=client.recv(1024).decode(FORMAT)
	print(msg)
	logginIn()
	# print(msg)

def logginIn():
	print("trying to log in")
	login_data=login()
	print("login data recieved",login_data)
	if(len(login_data)==1):
		return
	if len(login_data[0])==0:
		if login_data[1]=="signup":
			createSignup()
		if login_data[1]=="forgot":
			print("Reset password initiated")
			f=resetPassword()
	else:
		client.send("login".encode(FORMAT))
		client.send(str(":".join(login_data)).encode(FORMAT))
		msg=client.recv(1024).decode(FORMAT)
		if msg[:7]=="success":
			print("success recieved")
			try:
				resp=chat(client,msg[7:],1)
				print("control is here")
				print(msg[7:],"Left the chat")
				# client.send(str("left#"+msg[7:]).encode(FORMAT))
				client.close()
				

			except:
				pass
			return
		if msg=="failed":
			print("failed recieved")
			if wrong():
				logginIn()

def resetPassword():
	def getEmail():
		return entry1.get()
	def getOtp():
		return entry2.get()
	global validate
	validate=0
	def btn_reset():
		email=getEmail()
		global validate
		if validateEmail(email) and validate==0:
			client.send("reset".encode())
			client.send(email.encode())
			validate=1
			print("OTP request sent")

	def validateEmail(str):
		pattern=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b')
		if not re.fullmatch(pattern,str):
			canvas.itemconfig(4,state='normal')
			print("Invalid Email")
			return 0
		else:
			canvas.itemconfig(4,state='hidden')
			print("Valid Email")
			return 1

	def btn_otp():
		global validate
		if(validate==1):
			otp=getOtp()
			client.send("requestotp".encode(FORMAT))
			client.send(str(otp+"#"+getEmail()).encode(FORMAT))
			response=client.recv(1024).decode(FORMAT)
			print(response)
			if response=="invalidotp":
				canvas.itemconfig(5,state='normal')
				return
			else:
				canvas.itemconfig(5,state='hidden')

			if response[:4]!="Name":
				validate=0
				canvas.itemconfig(4,state='normal')
			else:
				# canvas.itemconfig(4,state='hidden')
				# root = Tk()
				# root.geometry("350x170")
				# T = Text(root, height = 5, width = 52)
				# l = Label(root, text = response)
				# l.config(font =("Courier", 14))
				# l.pack()
				# root.mainloop()
				showinfo(
                        title='New member joined',
                        message=response
                    )

	def btn_login():
		window.destroy()
		logginIn()

	window = Tk()

	window.geometry("1000x600")
	window.configure(bg = "#ffffff")
	canvas = Canvas(
		window,
		bg = "#ffffff",
		height = 600,
		width = 1000,
		bd = 0,
		highlightthickness = 0,
		relief = "ridge")
	canvas.place(x = 0, y = 0)

	background_img = PhotoImage(file = f"frontend\\resetPassword\\background.png")
	background = canvas.create_image(
		502.0, 294.0,
		image=background_img)

	
	entry1_img = PhotoImage(file = f"frontend\\resetPassword\\img_textBox1.png")
	entry1_bg = canvas.create_image(
		558.5, 214.5,
		image = entry1_img)

	entry1 = Entry(
		bd = 0,
		bg = "#eeecec",
		highlightthickness = 0,font=('Ubuntu 16'))

	entry1.place(
		x = 366.0, y = 192,
		width = 385.0,
		height = 43)

	entry2_img = PhotoImage(file = f"frontend\\resetPassword\\img_textBox2.png")
	entry2_bg = canvas.create_image(
		466.0, 368.5,
		image = entry2_img)

	entry2 = Entry(
		bd = 0,
		bg = "#eeecec",
		highlightthickness = 0,font=('Ubuntu 16'))

	entry2.place(
		x = 371.0, y = 346,
		width = 190.0,
		height = 43)

	img0 = PhotoImage(file = f"frontend\\resetPassword\\img0.png")
	b0 = Button(
		image = img0,
		borderwidth = 0,
		highlightthickness = 0,
		command = btn_reset,
		relief = "flat")

	b0.place(
		x = 351, y = 259,
		width = 151,
		height = 53)

	img1 = PhotoImage(file = f"frontend\\resetPassword\\img1.png")
	b1 = Button(
		image = img1,
		borderwidth = 0,
		highlightthickness = 0,
		command = btn_otp,
		relief = "flat")

	b1.place(
		x = 627, y = 338,
		width = 151,
		height = 53)
	img2 = PhotoImage(file = f"frontend\\login\\img2.png")
	b2 = Button(
	image = img2,
	borderwidth = 0,
	highlightthickness = 0,
	command = btn_login,
	relief = "flat")

	b2.place(
	x = 366, y = 420,
	width = 151,
	height = 53)

	canvas.create_text(
	666.5, 261.0,
	text = "Invalid Email ID!",
	fill = "#df1818",
	font = ("None", int(12.0)),
	state="hidden")
	canvas.create_text(
	405.5, 410.0,
	text = "Invalid OTP!",
	fill = "#df1818",
	font = ("None", int(12.0)),
	state="hidden")

	window.resizable(False, False)
	window.mainloop()


	
logginIn()
exit()