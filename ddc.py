# -*- coding: utf-8 -*-

from socket import *
import time
import json


#################################
# 测试设备的mac
_id = "2514A4C1387E88AC"
# 网关ip
_ip = "192.168.1.194"
# 总共测试多少次
_time = 5
#################################


tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
_all = 0
_success = 0

while _time:
    _json = {
        "sourceId":"0",
        "requestType":"cmd",
        "serialNum":-1,
        "id": _id,
        "attributes": {"SW1": "ON"}
    }

    ret = tcp_client_socket.send(json.dumps(_json).encode())
    print("send: %s"%json.dumps(_json))
    _time -= 1
    _all += 1
    time.sleep(1)

    data = tcp_client_socket.recv(1024)
    print("recv: %s"%data)
    _json = json.loads(data)
    _success += 1 if _json.get("stateCode", 0) == 1 else 0

print("丢包率:%.2f %%"%(100*float(_all-_success)/_all))
