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
    558.5, 214.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry0.place(
    x = 366.0, y = 192,
    width = 385.0,
    height = 43)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    558.5, 214.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry1.place(
    x = 366.0, y = 192,
    width = 385.0,
    height = 43)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    565.5, 284.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry2.place(
    x = 373.0, y = 262,
    width = 385.0,
    height = 43)

canvas.create_text(
    447.0, 460.5,
    text = "Forgot Password?",
    fill = "#3b2e5f",
    font = ("Chivo-Regular", int(22.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 490, y = 359,
    width = 151,
    height = 53)

window.resizable(False, False)
window.mainloop()
