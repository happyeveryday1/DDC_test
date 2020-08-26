# -*- coding: utf-8 -*-

from socket import *
import time
import json


#################################
# 测试设备的mac
_id = "68F746E31A7CCB55"
# 网关ip
_ip = "192.168.100.1"
#################################


tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))

a=[{"SW1": "ON","SCE":1},{"SW1": "OFF","SCE":2}]
while len(a)>0:

    for i in a:
        print(i)
        _json_on = {
            "sourceId":"0",
            "requestType":"cmd",
            "serialNum":-1,
            "id": _id,
            "attributes": i
        }


        ret = tcp_client_socket.send(bytes(json.dumps(_json_on).encode('utf-8')))
        data = tcp_client_socket.recv(1024)
        print(data.decode())
        del(a[0])
        time.sleep(2)
