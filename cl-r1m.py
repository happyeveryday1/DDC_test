from socket import *
import time
import json
# 测试设备的mac
_id = "00124B000E905FC8"
# 网关ip
_ip = "10.101.3.31"

tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
_time = 15000

while _time:

    _json1 = {
        "sourceId": "0",
        "requestType": "cmd",
        "serialNum": -1,
        "id": _id,
        "attributes": {"RDK": "SAV", 'SWI': "ON"}
    }
    _json2 = {
        "sourceId": "0",
        "requestType": "cmd",
        "serialNum": -1,
        "id": _id,
        "attributes": {"RDK": "SAV", 'SWI': "OFF"}
    }

    ret = tcp_client_socket.send(json.dumps(_json1).encode('utf-8'))
    data=tcp_client_socket.recv(1024)
    print(data.decode())
    time.sleep(10)
    ret = tcp_client_socket.send(json.dumps(_json2).encode('utf-8'))
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    _time -= 1
    time.sleep(5)

