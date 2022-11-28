import imghdr
from tkinter import *
from PIL import ImageTk, Image
response=['','']
def login():
    def btn_login():
        global response
        print("Button Clicked")
        print(getEmail())
        print(getPassword())
        response=[getEmail(),getPassword()]
        window.destroy()

    def btn_signup():
        global response
        response=["","signup"]
        window.destroy()
    
    def btn_forgot():
        global response
        response=["","forgot"]
        window.destroy()

    def getEmail():
        return entry1.get()
    def getPassword():
        return entry2.get()
    
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

    background_img = PhotoImage(file = f"frontend\\login\\background.png")
    background = canvas.create_image(
        502.0, 294.0,
        image=background_img)

    entry1_img = PhotoImage(file = f"frontend\\login\\img_textBox1.png")
    entry1_bg = canvas.create_image(
        558.5, 214.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#eeecec",
        highlightthickness = 0)
    entry1.focus_set()

    entry1.place(
        x = 366.0, y = 192,
        width = 385.0,
        height = 43)

    entry2_img = PhotoImage(file = f"frontend\\login\\img_textBox2.png")
    entry2_bg = canvas.create_image(
        565.5, 284.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#eeecec",
        highlightthickness = 0,
        show="*")

    entry2.place(
        x = 373.0, y = 262,
        width = 385.0,
        height = 43)

    img0 = PhotoImage(file = f"frontend\\login\\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_forgot,
        relief = "flat")

    b0.place(
        x = 346, y = 445,
        width = 191,
        height = 18)

    img1 = PhotoImage(file = f"frontend\\login\\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_signup,
        relief = "flat")

    b1.place(
        x = 582, y = 359,
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
        x = 397, y = 359,
        width = 151,
        height = 53)

    window.resizable(False, False)
    window.mainloop()
    return response


def w_btn():
    print("Button Clicked")

def wrong():
    window1 = Tk()

    window1.geometry("600x360")
    window1.configure(bg = "#ffffff")
    canvas = Canvas(
        window1,
        bg = "#ffffff",
        height = 360,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"frontend\\login\\bg2.png")
    background = canvas.create_image(
        300.0, 180.0,
        image=background_img)

    img0 = PhotoImage(file = f"frontend\\login\\img5.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = w_btn,
        relief = "flat")

    b0.place(
        x = 373, y = 231,
        width = 134,
        height = 46)

    window1.resizable(False, False)
    window1.mainloop()

# login()