import tkinter as tk

def button_clicked():
    print("Button Clicked")

window = tk.Tk()

window.geometry("1000x600")
window.configure(bg="#ffffff")

canvas = tk.Canvas(
    window,
    bg="#ffffff",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

background_img = tk.PhotoImage(file="background.png")
background = canvas.create_image(502.0, 294.0, image=background_img)

entry_img = tk.PhotoImage(file="img_textBox0.png")
entry_bg = canvas.create_image(558.5, 214.5, image=entry_img)

entry = tk.Entry(
    bd=0,
    bg="#eeecec",
    highlightthickness=0
)

entry.place(x=366.0, y=192, width=385.0, height=43)

img0 = tk.PhotoImage(file="img0.png")
button0 = tk.Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked,
    relief="flat"
)

button0.place(x=346, y=445, width=191, height=18)

img1 = tk.PhotoImage(file="img1.png")
button1 = tk.Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked,
    relief="flat"
)

button1.place(x=582, y=359, width=151, height=53)

img2 = tk.PhotoImage(file="img2.png")
button2 = tk.Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked,
    relief="flat"
)

button2.place(x=397, y=359, width=151, height=53)

window.resizable(False, False)
window.mainloop()
