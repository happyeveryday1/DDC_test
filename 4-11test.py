# -*- coding: utf-8 -*-
import socket
import select
import json
import time
#################################
# 网关ip
_ip = "10.101.3.31"
# 总共测试多少次
_time = 5
# 计量开启后，等多少秒再读取设备状态
swiondelay = 10
# 计量关闭后，等多少秒再开计量
swioffdelay = 10
# ack最长等待时间
_recvtimeout = 20
# 计量开关mac
_id = "00124B000E905FC8"
# 受控设备的mac和名字的映射
_mac = "00124B001EBFAC79"

_list=[]
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

_all = 0
_success=0
recvtimeout = 0
r1m_state = 0
_json_on = {
    "sourceId":"0",
    "requestType":"cmd",
    "serialNum": -1,
    "id": _id,
    "attributes": {"SWI": "ON"}
}
_json_off = {
    "sourceId":"0",
    "requestType":"cmd",
    "serialNum": -1,
    "id": _id,
    "attributes": {"SWI": "OFF"}
}
while _time >= 0:

    r, _, _ = select.select(r_inputs, w_inputs, e_inputs, 1)
    # 开计量
    if recvtimeout == 0 and r1m_state == 0:
        ret = tcp_client_socket.send((json.dumps(_json_on)+"\n").encode('utf-8'))
        print("第%s次开计量"%((5-_time)+1))
        print("-------------------------------------\n开计量: ")
        _time -= 1
        r1m_state = 1
        time.sleep(swiondelay)

    # 发送读取设备状态指令
    if recvtimeout == 0 and r1m_state == 1:
        _json_rdk = {
            "sourceId":"0",
            "requestType":"cmd",
            "serialNum":_mac ,
            "id":_mac,
            "attributes": {"RDK": "TYP"},
        }
        ret = tcp_client_socket.send((json.dumps(_json_rdk)+"\n").encode('utf-8'))
        #print("读取设备信息: %s"%json.dumps(_json_rdk))
        _list.append(json.dumps(_json_rdk))
    else:
        recvtimeout = _recvtimeout

    # 接受ack
    if recvtimeout >= 0:
        for event in r:
            _data = event.recv(10240).decode("utf-8")
            json_packets = _data.split("\n")
            for data in json_packets:
                data = data.strip()
                if data:
                    _json = json.loads(data)
                    # 根据流水号记录成功的ack
                    if _json.get("serialNum", "") != "-1" and _json.get("stateCode", "") == 1 :
                        #print("设备ack回应: %s"%data)
                        _success+=1
                        #print(len(_success))
        else:
            time.sleep(1)
            recvtimeout -= 1

    #关计量
    if recvtimeout == 0 and r1m_state == 1:
        r_list, w_list, e_list = select.select(r_inputs, w_inputs, e_inputs, 1)
        ret = tcp_client_socket.send((json.dumps(_json_off)+"\n").encode('utf-8'))
        print("\n关计量: %s\n-------------------------------------\n"%json.dumps(_json_off))
        r1m_state = 0
        recvtimeout = 0
        _all += 1
        time.sleep(swioffdelay)


mylog = open('recode.log', mode = 'a',encoding='utf-8')
for mac in _success:
    print("%s的丢包率:%.2f %%"%(_dict[mac], 100*float(_all-_success[mac])/_all),file=mylog)
    #f.write("%s的丢包率:%.2f %%"%(_dict[mac], 100*float(_all-_success[mac])/_all))

#mylog = open('recode.log', mode = 'a',encoding='utf-8')
# for i in range(10):
#     print("sdjlahjljag", file=mylog)
mylog.close()