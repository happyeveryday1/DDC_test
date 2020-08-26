# -*- coding: utf-8 -*-

from socket import *
import time
import json


#################################
# 测试设备的mac
_id = "2514A4C1387E88AC"
# 网关ip
_ip = "192.168.1.194"
#################################


tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
_time = 15000

while _time:
    _json_on = {
        "sourceId":"0",
        "requestType":"cmd",
        "serialNum":-1,
        "id": _id,
        "attributes": {"SW1": "ON"}
    }
    print(bytes(json.dumps(_json_on).encode('utf-8')))
    ret = tcp_client_socket.send(bytes(json.dumps(_json_on).encode('utf-8')))
    data = tcp_client_socket.recv(10240)
    print(data.decode())
    time.sleep(5)

    _time -= 1
    time.sleep(1)
