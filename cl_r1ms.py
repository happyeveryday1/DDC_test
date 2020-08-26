from socket import *
import time
import json


#################################
# 测试设备的mac
_id = "00124B001D132D23"
# 网关ip
_ip = "10.101.3.31"
#################################

tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
# times = 0
# _all = 0
# _success = 0
while True:

    # ret = tcp_client_socket.send(bytes(json.dumps(_json1).encode('utf-8')))
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    _json = json.loads(data)
    print(_json)


#print("丢包率:%.2f %%"%(100*float(times/_all)))
