from audioop import add
import socket
from datetime import datetime
import threading

start_time = datetime.now()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created successfully")

port=12345
host_ip=socket.gethostbyname(socket.gethostname())
host_ip="172.16.184.76"
s.bind((host_ip,port))
print("socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

i=0
msg="Thank you for connecting"
clos=1



# while clos:
#     while True:
#         end_time = datetime.now()

#         if str(end_time - start_time)[5]==4:
#             print("Timeout")
#             break

#         c,addr=s.accept()

#         print('got connection from',addr)
#         try:
#             c.send(msg.encode())
#         except:
#             pass
#         try:
#             msg=c.recv(1024).decode()
#         except:
#             pass
#         print(msg,"RECIEVED")

#         if msg=="bye":
#             try:
#                 c.send(msg.encode())
#             except:
#                 pass
#         c.close()
#         if msg=="bye":
#             clos=0
#             break

# dic={1:1,2:2,3:3}
# print(dic.keys())
# exit()

connection_list={}
msg="thanks for connecting"

def recieve(c):
    while True:
        try:
            rmsg=c.recv(1024).decode()
            if rmsg=="end":
                break
            if len(rmsg)>0:
                print("----->",rmsg)
        except:
            pass

def rcv_msg(connect_from):
    while True:
        try:
            return connect_from.recv(1024).decode()
        except:
            pass
def snd_msg(connect_to,msg):
    while True:
        try:
            if len(msg)>0:
                connect_to.send(msg.encode())
                break
        except:
            pass

def chat(connect_from,connect_to):
    # msg=""
    con_from=connect_from
    con_to=connect_to
    connect_from=connection_list[connect_from][0]
    connect_to=connection_list[connect_to][0]
    while True:
        try:
            rmsg=connect_from.recv(1024).decode()
            print("recieved from ",con_from)
            if(rmsg=="end"):
                connect_to.send(str("Chat ended with "+con_from).encode())
                connect_from.send(str("Chat ended with "+con_to).encode())
                connect_from.close()
                connect_to.close()
                break
            rmsg=con_from+" : "+rmsg
            connect_to.send(rmsg.encode())
            print(" send to ",con_to)
        except:
            pass

def thread_connect(c,addr):
    print("Recieved connection from",addr)
    c.send("You are connected".encode())

    c.send("Enter your ID".encode())

    name=c.recv(1024).decode()

    connection_list[name]=[c,addr]



    if (len(connection_list)==1):
        c.send("No One is Online".encode())

    while (len(connection_list)<=1):
        pass
    else:
        c.send("Press to chat\n".encode())
        key_list=list(connection_list.keys())
        k=0
        tmp=[]
        for i in range(len(key_list)):
            if(key_list[i]!=name):
                c.send(str(str(k+1)+". "+key_list[i]+"\n").encode())
                k+=1
                tmp.append(key_list[i])
            
        key_list=tmp
        
        while True:
            rmsg=c.recv(1024).decode()
            
            try:
                rmsg=int(rmsg)-1
                if 0<=int(rmsg)<len(key_list):
                    connect_to=key_list[int(rmsg)]
                    connect_from=name
                    c.send(str(name+" connected to "+str(key_list[int(rmsg)])).encode())
                    th=threading.Thread(target=chat,args=(connect_to,connect_from,))
                    th.start()
                    th.join()
                    del connection_list[name]
                    c.close()
                    break
                else:
                    c.send("Enter valid Option".encode())

            except:
                c.send("Enter valid Options".encode())


    # print('got connection from',addr)
    # print("Available connections are")
    # for k in connection_list.keys():
    #     print(connection_list[k][1])
    # # try:
    # #     msg=c.recv(1024).decode()
    # # except:
    # #     pass
    # c.send(msg.encode())
    # t1=threading.Thread(target=recieve,args=(c))
    # t1.start()
    # t1.join()
    # del connection_list[name]
    # c.close()

while True:
    c,addr=s.accept()
    t1 = threading.Thread(target=thread_connect, args=(c,addr))
    t1.start()
    



