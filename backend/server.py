import socket
from datetime import datetime
import threading

start_time = datetime.now()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created successfully")

port=12345
# host_ip=input("Enter Server IP Address")
host_ip="172.16.184.76"

s.bind((host_ip,port))
print("socket binded to %s"%(port))

s.listen(5)
print("Socket is listening")

thread_connection={}
while True:
    c,addr=s.accept()
    thread_connection[addr]=[]
    thread_connection[addr].append(c)

    friend_list=open(str(addr+"_friendlist.csv"),"a")
    thread_connection[addr].append(friend_list)




