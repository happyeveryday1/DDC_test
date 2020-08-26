# -*- coding: utf-8 -*-

import socket
import select
import json


#################################
# 网关ip
_ip = "192.168.1.194"
#################################


tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_client_socket.setblocking(False)

try:
    tcp_client_socket.connect((_ip, 8888))
except Exception as e:
    print(e)

r_inputs = set()
r_inputs.add(tcp_client_socket)
w_inputs = set()
w_inputs.add(tcp_client_socket)
e_inputs = set()
e_inputs.add(tcp_client_socket)

while True:
    try:
        r, _, _ = select.select(r_inputs, w_inputs, e_inputs, 1)
        for event in r:
            _data = event.recv(10240).decode("utf-8")
            json_packets = _data.split("\n")
            for data in json_packets:
                data = data.strip()
                if data:
                    _json = json.loads(data)
                    print ("recv json: %s"%(_json))
                    # and do sth.

    except OSError as e:
        print(e)
