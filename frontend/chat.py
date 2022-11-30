import os
import sys
import threading
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
FORMAT = "utf-8"
flag=1
active_list=[]
def chat(client,name,initiate):
    global flag
    print("client is ",client,name,flag)

    def recvMsg(client):
        global flag
        # global chat_msg
        while True:
            try:
                if flag==0:
                    print("recv closed")
                    return
                # client.recv(chat_msg.decode(FORMAT))
                # print("waiting for msg")
                chat_msg=client.recv(1024).decode(FORMAT)
                # print("recieved msg ",chat_msg,"  ")
                if chat_msg[:3]=="msg":
                    # entry1.delete(0,END)
                    msg_decode=chat_msg.split("#")
                    recieved_name0=msg_decode[1]
                    recieved_msg=msg_decode[2]

                    textCons.config(state=NORMAL)
                    recieved_name1=recieved_name0.split(" ")[0]
                    if(recieved_name0==name):
                        # textCons.config(fg="red")
                        formatted_text="{:<14} : {}\n".format("[YOU]",recieved_msg)
                    else:
                    #     textCons.config(fg="black")
                        formatted_text="{:<14} : {}\n".format(str("["+recieved_name1+"]"),recieved_msg)

                    textCons.insert(END,
                        "{:<15} : {} \n\n".format(recieved_name1,recieved_msg))
                        
                    textCons.config(state=DISABLED)
                    textCons.see(END)
                if chat_msg[:chat_msg.find("#")]=="client" and chat_msg[chat_msg.find("#")+1:]!=name:
                    # print(chat_msg[chat_msg.find("#"):],"Joined the chat")
                    recieved_name1=chat_msg.split("#")[1]
                    active_list.append(recieved_name1.split(" ")[0])

                    textCons.config(state=NORMAL)
                    formatted_text="{:^120}\n".format(str(recieved_name1+" joined the chat"))
                    textCons.insert(END,
                        formatted_text)
                        
                    textCons.config(state=DISABLED)
                    textCons.see(END)
                if chat_msg[:chat_msg.find("#")]=="active":
                    # print("active detected")
                    active=chat_msg.split("#")
                    active=active[1:]
                    # print("active list is",active)
                    formatted_text=""
                    for curr in active:
                        formatted_text+="\u25CF "+curr.split(" ")[0]+"\n"
                    time.sleep(0.5)
                    # print("writing")
                    textCons1.config(state=NORMAL)
                    textCons1.delete("1.0","end")
                    textCons1.insert(END,
                        formatted_text)
                        
                    textCons1.config(state=DISABLED)

                    textCons1.see(END)
                    # print("okk")

                if(chat_msg[:chat_msg.find("#")])=="type":
                    typing(chat_msg[chat_msg.find("#"):])
                if (chat_msg[:chat_msg.find("#")])=="left":

                    recieved_name1=chat_msg.split("#")[1]
                    textCons.config(state=NORMAL)
                    formatted_text="{:^120}\n".format(str(recieved_name1+" left the chat"))
                    textCons.insert(END,
                        formatted_text)
                        
                    textCons.config(state=DISABLED)
                    textCons.see(END)

                    # try:
                    #     active_list.remove(recieved_name1.split(" ")[0])
                    # except:
                    #     print("No one was present")

                    # textCons1.delete(0,END)
                    # textCons1.config(state=NORMAL)
                    # formatted_text=""
                    # for active in active_list:
                    #     formatted_text+="\u26AB "+active+"\n"
                    # textCons1.insert(END,
                    #     formatted_text)
                        
                    # textCons1.config(state=DISABLED)
                    # textCons.see(END)
            
            except:
                pass
        return 

    recv_thread=threading.Thread(target=recvMsg,args=(client,))
    recv_thread.start()
    for thread in threading.enumerate(): 
        print(thread.name)
    def btn_clicked():
        window.destroy()
        global flag
        flag=0
        client.send("exit".encode(FORMAT))
        # print("Button Clicked")
        return


    window = Tk()

    window.geometry("1000x600")
    window.title("CHATROOM")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#d1d1d1",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # window.wm_attributes('-transparentcolor', '#d1d1d1')
    labelHead = Label(window,
                                bg="white",
                                fg="black",
                                # take username from singup or singin
                                text=name,
                                font="Helvetica 13 bold",
                                pady=5)
    labelHead.place(x=400,y=40)
    labelHead1 = Label(window,
                                bg="white",
                                fg="Green",
                                # take username from singup or singin
                                text="\u23F3",
                                font="Helvetica 13 bold",
                                pady=5)
    labelHead1.place(x = 810, y = 128)
    labelHead2 = Label(window,
                                bg="white",
                                fg="blue",
                                # take username from singup or singin
                                text="Active ",
                                font="Helvetica 13 bold",
                                pady=5)
    labelHead2.place(x = 840, y = 128)

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
        # print(msg_encode,"sent")

        entry0.delete(0,END)

    img0 = PhotoImage(file = f"frontend\\chatWindow\\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:getthemassage(),
        relief = "flat")

    # print(entry0.get())
    b0.place(
        x = 811, y = 526,
        width = 142,
        height = 58)

    def select_file():
        filetypes = (
            ('All files', '*.*'),
            ('text files', '*.txt')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )

        # print(filename)
        file=open(filename,"rb")
        file_size=os.path.getsize(filename)
        typo=filename.split(".",1)
        kk=typo[1]
        textCons.config(state=NORMAL)
   
        textCons.insert(END,name+ filename+"\n\n")

        textCons.config(state=DISABLED)
        textCons.see(END)
        client.send(("ATTACHMENT#").encode(FORMAT))
        # return
        time.sleep(1)
        client.send(("recived."+kk).encode(FORMAT))
        # print(("recived."+kk),"Sent")
        time.sleep(3)
        client.send(str(file_size).encode(FORMAT))
        # print(str(file_size),"Sent")
        time.sleep(3)

        data=file.read()
        client.sendall(data)
        time.sleep(1)
        # print("file bits sent")
        client.send(b"<END>")
        file.close()
        # client.close()
        return
            
        

    img1 = PhotoImage(file = f"frontend\\chatWindow\\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:select_file(),
        relief = "flat")
    # background_img = PhotoImage(file = f"frontend\\login\\background.png")
    # background = canvas.create_image(
    #     502.0, 294.0,
    #     image=background_img)
    # background.attributes('-alpha',0.5)
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

    # entry1_img = PhotoImage(file = f"frontend\\chatWindow\\img_textBox1.png")
    # entry1_bg = canvas.create_image(
    #     474.0, 74.5,
    #     image = entry1_img)

    entry1 = Label(window,
                        bg="white",
                        fg="black",
                        # take username from singup or singin
                        text="",
                        font="Helvetica 10 italic",
                        pady=5)

    entry1.place(
        x = 80, y = 80,
        width = 150,
        height = 14)

    textCons = Text(window,
                                width=18,
                                height=2,
                                bg="#d1d1d1",
                                fg="black",
                                font="Helvetica 10",
                                padx=5,
                                pady=5)

    textCons.place(
        x = 89, y = 128,
        width = 703,
        height = 389)
    
    textCons1 = Text(window,
                            width=18,
                            height=2,
                            bg="#f7e4e4",
                            fg="#3b5998",
                            font="Helvetica 13",
                            padx=10,
                            pady=7)

    textCons1.place(
        x = 802, y = 155,
        width = 170,
        height = 250)

    # scrolbar
    scrollbar = Scrollbar(textCons)
    scrollbar1 = Scrollbar(textCons1)
    
            # place the scroll bar
            # into the gui window
    scrollbar.place(relheight=1,
                            relx=0.974)
    scrollbar1.place(relheight=1,
                            relx=0.974)
    def threadTyping(client):
        print("typing initiated")
        prevlen=0
        while True:
            if flag==0:
                # print("typing closed")
                return
            # print("Entry is",entry0.get())
            currlen=len(entry0.get())
            if prevlen!=currlen:
                # print(name ,"is typing")
                client.send(str("type#"+str(name)).encode(FORMAT))
                prevlen=currlen
            time.sleep(0.7)

    def typing(typer):
        # print(typer,"is typing")
        if name!=typer[1:]:
            nm=typer[1:].split(" ")[0]
            entry1.config(text=str(nm+" is typing"))
            time.sleep(0.7)
            entry1.config(text="")

    thread_typing=threading.Thread(target=threadTyping,args=(client,))
    thread_typing.start()

    scrollbar.config(command=textCons.yview)
    textCons.config(state=DISABLED)
    window.resizable(False, False)
    window.mainloop()

    # print("exitted")
    # global flag
    flag=0
    client.send(str("exit#"+name).encode(FORMAT))
    # print("exitted sent","exit#"+name)
    # exit()
    return "exit"
    # sys.exit()