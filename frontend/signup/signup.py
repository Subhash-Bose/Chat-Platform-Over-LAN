from tkinter import *


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    502.0, 294.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    559.5, 193.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry0.place(
    x = 367.0, y = 171,
    width = 385.0,
    height = 43)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    559.5, 263.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry1.place(
    x = 367.0, y = 241,
    width = 385.0,
    height = 43)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    559.5, 263.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry2.place(
    x = 367.0, y = 241,
    width = 385.0,
    height = 43)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    566.5, 333.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry3.place(
    x = 374.0, y = 311,
    width = 385.0,
    height = 43)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 453, y = 403,
    width = 228,
    height = 53)

window.resizable(False, False)
window.mainloop()
