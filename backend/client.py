import socket
from datetime import datetime
import threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start_time = datetime.now()

port=12345
host_ip=socket.gethostbyname(socket.gethostname())
host_ip="172.16.184.76"
s.connect((host_ip,port))
# s.connect((socket.gethostbyname(socket.gethostname()),port))

print("You can chat Now")
clos=1

# while clos:
#     while True:
#         end_time = datetime.now()
#         if str(end_time - start_time)[5]==4:
#             print("Timeout")
#             break
#         while True:
#             if str(end_time - start_time)[5]==2:
#                 print("Timeout")
#                 break
#             try:
#                 print("    ---> "+s.recv(1024).decode())
#                 break
#             except:
#                 pass
#         msg=input()
#         try:
#             s.send(msg.encode())
#         except: 
#             print("Cannot send msg")

#         s.close()
#         s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#         s.connect((host_ip,port))

#         if msg=="bye":
#             s.close()
#             clos=0
#             break
def snd(s):
    while True:
        smsg=input()
        s.send(smsg.encode())
        if smsg=="end":
            # s.close()
            thread_call()
            break

def recieve(s):
    while True:
        try:
            rmsg=s.recv(1024).decode()
            if len(rmsg)>0:
                print("--->",rmsg)
        except:
            pass

def thread_call():
    t1=threading.Thread(target=recieve,args=(s,))
    t2=threading.Thread(target=snd,args=(s,))
    t1.start()
    t2.start()


rmsg=s.recv(1024).decode()
print(rmsg)

rmsg=s.recv(1024).decode()
print(rmsg)

name=input()
s.send(name.encode())


t1=threading.Thread(target=recieve,args=(s,))
t2=threading.Thread(target=snd,args=(s,))
t1.start()
t2.start()

print("Press end and enter to exit")
# while True:
#     smsg=input()
#     # print()
#     if smsg=="end":
#         s.close()
#         break