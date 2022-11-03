import socket
from datetime import datetime
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start_time = datetime.now()

port=12345
host_ip=socket.gethostbyname(socket.gethostname())
host_ip="172.16.184.76"
s.connect((host_ip,port))
# s.connect((socket.gethostbyname(socket.gethostname()),port))
