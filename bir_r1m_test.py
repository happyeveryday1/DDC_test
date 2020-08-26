# -*- coding: utf-8 -*-
import socket
import select
import json
import time
#################################
# 网关ip
_ip = "192.168.1.216"
# 总共测试多少次
_time = 5
# 计量开启后，等多少秒再读取设备状态
swiondelay = 20
# 计量关闭后，等多少秒再开计量
swioffdelay = 5
# ack最长等待时间
_recvtimeout = 20
# 计量开关mac
_id = "00124B000E905FC8"
#接收到的数据
_recv_data=[]
# 受控设备的mac和名字的映射
_dict = {
    #"2001A4C13854056D": "三件面板",
    "00124B001D3F2D6D":"红外转发器1",#1
    "00124B001D65C0E4":"红外转发器2",#2
    "00124B001D3F2915":"红外转发器3",#3
    "00124B001D3F2E1F":"红外转发器4",#4
    "00124B001D3F2C33":"红外转发器5",#5
    "00124B00210BD853":"红外转发器6",#6
    "00124B001D3F2877":"红外转发器7",#7
    "00124B001D3F2A26":"红外转发器8",#8
    "00124B00210BD2BA":"红外转发器9",#9
    "00124B00210BD57E":"红外转发器10",#10
    "00124B001D3F2907":"红外转发器11",#11
    "00124B001D3F2976":"红外转发器12",#12
    "00124B001D3F2C75":"红外转发器13",#13
    "00124B001D3F2D7D":"红外转发器14",
    "00124B00210BCF98":"红外转发器15",
    "00124B001D3F2C65":"红外转发器16",
    "00124B001D659ABD":"红外转发器17",
    "00124B00210BD811":"红外转发器18",
    "00124B001D3F295C":"红外转发器19",
    "00124B00210BD576":"红外转发器20",
    "00124B001D3F2A7A":"红外转发器21",
    "00124B00210BD55D":"红外转发器22",
    "00124B00210BD2DF":"红外转发器23",
    "00124B00210BD2E7":"红外转发器24",
    "00124B00210BD810":"红外转发器25",
    "00124B00210BD2CD":"红外转发器26",
    "00124B001D3F2A27":"红外转发器27",
    "00124B001D3F2911":"红外转发器28",
    "00124B00210BD844":"红外转发器29",
    "00124B001D3F285F":"红外转发器30",
    "00124B001D3F2909":"红外转发器31",
    "00124B001D65BB2D":"红外转发器STG1",
    "00124B001D3F2B79":"红外转发器STG2",
    "00124B001D3F8750":"红外转发器STG3",
    "00124B001D65BEEB":"红外转发器STG4",
    "00124B001D659AB0":"红外转发器STG5",
    "00124B001EC0C312":"红外转发器STG6",
    "00124B001D3F2317":"红外转发器STG7",
}
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
_success = dict([(mac, 0) for mac in _dict])
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
    try:
        r, _, _ = select.select(r_inputs, w_inputs, e_inputs, 1)
        # 开计量
        if recvtimeout == 0 and r1m_state == 0:
            #print("第%s次开计量" % ((10 - _time) + 1))
            ret = tcp_client_socket.send((json.dumps(_json_on)+"\n").encode('utf-8'))
            #print("-------------------------------------\n开计量: %s\n"%json.dumps(_json_on))
            _time -= 1
            r1m_state = 1
            time.sleep(swiondelay)

        # 发送读取设备状态指令
        if recvtimeout == 0 and r1m_state == 1:
            for mac in _success:

                _json_rdk = {
                    "sourceId":"0",
                    "requestType":"cmd",
                    "serialNum": mac,
                    "id": mac,
                    "attributes": {"RDK": "TYP"}
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
                        if _json.get("serialNum", "") != "-1" and _json.get("stateCode", "") == 1 and _json.get("serialNum", "") in _success:

                            #print("设备ack回应: %s"%data)
                            _recv_data.append(data)
                            _success[_json.get("id", "")] += 1

            else:
                time.sleep(1)
                recvtimeout -= 1

        #关计量
        if recvtimeout == 0 and r1m_state == 1 :
            #_recv_data.clear()
            r_list, w_list, e_list = select.select(r_inputs, w_inputs, e_inputs, 1)
            ret = tcp_client_socket.send((json.dumps(_json_off)+"\n").encode('utf-8'))
            print("\n关计量: %s\n-------------------------------------\n"%json.dumps(_json_off))
            r1m_state = 0
            recvtimeout = 0
            _all += 1
            time.sleep(swioffdelay)

    except OSError as e:
        print(e)
mylog = open('recode.log', mode = 'a',encoding='utf-8')
for mac in _success:
    print("%s的丢包率:%.2f %%"%(_dict[mac], 100*float(_all-_success[mac])/_all),file=mylog)
mylog.close()