import threading
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
FORMAT = "utf-8"
def chat(client,name):
    def recvMsg(client):
        # global chat_msg
        while True:
            try:
                # client.recv(chat_msg.decode(FORMAT))
                print("waiting for msg")
                chat_msg=client.recv(1024).decode(FORMAT)
                if chat_msg[:3]=="msg":
                    msg_decode=chat_msg.split("#")
                    recieved_name=msg_decode[1]
                    recieved_msg=msg_decode[2]

                    textCons.config(state=NORMAL)
                    recieved_name=recieved_name[:recieved_name.find(" ")]
                    textCons.insert(END,
                        "{:<15} : {} \n\n".format(recieved_name,recieved_msg))
                        
                    textCons.config(state=DISABLED)
                    textCons.see(END)
            except:
                pass
    recv_thread=threading.Thread(target=recvMsg,args=(client,))
    recv_thread.start()
    def btn_clicked():
        window.destroy()
        print("Button Clicked")


    window = Tk()

    window.geometry("1000x600")
    window.title("CHATROOM")
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


    labelHead = Label(window,
                                bg="white",
                                fg="black",
                                # take username from singup or singin
                                text=name,
                                font="Helvetica 13 bold",
                                pady=5)
    labelHead.place(relwidth=1)

    entry0_img = PhotoImage(file = f"frontend\chatWindow\img_textBox0.png")
    entry0_bg = canvas.create_image(
        384.0, 561.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#a4f089",
        highlightthickness = 0,font="Helvetica 13")

    entry0.place(
        x = 109.0, y = 539,
        width = 550.0,
        height = 43)
    def getthemassage():
        k=entry0.get()
        msg_encode="msg#"+name+"#"+k
        client.send(msg_encode.encode(FORMAT))

        entry0.delete(0,END)
        # textCons.config(state=NORMAL)
        # # stri="{} : {} \n\n".format(name,k)
        # textCons.insert(END,
        #                 "{} : {} \n\n".format(name,k))

        # textCons.config(state=DISABLED)
        # textCons.see(END)




    img0 = PhotoImage(file = f"frontend\\chatWindow\\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:getthemassage(),
        relief = "flat")
    print(entry0.get())
    b0.place(
        x = 811, y = 526,
        width = 142,
        height = 58)

    def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )

        print(filename)


        import os
        import socket
        client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        PORT = 5000
        SERVER = "172.16.181.29"
        ADDRESS = (SERVER, PORT)
        client.connect(ADDRESS)
        file=open(filename,"rb")
        file_size=os.path.getsize(filename)
        typo=filename.split(".",1)
        kk=typo[1]
        textCons.config(state=NORMAL)
    
        textCons.insert(END,
                        "NAME=> "+ filename+"\n\n")

        textCons.config(state=DISABLED)
        textCons.see(END)
        client.send(("recived."+kk).encode())
        client.send(str(file_size).encode())


        data=file.read()
        client.sendall(data)
        client.send(b"<END>")
        file.close()
        client.close()

    img1 = PhotoImage(file = f"frontend\\chatWindow\\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:select_file(),
        relief = "flat")

    b1.place(
        x = 848, y = 427,
        width = 84,
        height = 80)

    img2 = PhotoImage(file = f"frontend\\chatWindow\\img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 848, y = 55,
        width = 92,
        height = 39)

    entry1_img = PhotoImage(file = f"frontend\\chatWindow\\img_textBox1.png")
    entry1_bg = canvas.create_image(
        474.0, 74.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0,font="Ubantu 15")

    entry1.place(
        x = 125, y = 45,
        width = 698,
        height = 57)

    textCons = Text(window,
                                width=18,
                                height=2,
                                bg="white",
                                fg="black",
                                font="Helvetica 10",
                                padx=5,
                                pady=5)

    textCons.place(
        x = 89, y = 128,
        width = 703,
        height = 389)

    # scrolbar
    scrollbar = Scrollbar(textCons)

            # place the scroll bar
            # into the gui window
    scrollbar.place(relheight=1,
                            relx=0.974)

    scrollbar.config(command=textCons.yview)
    textCons.config(state=DISABLED)
    window.resizable(False, False)
    window.mainloop()
