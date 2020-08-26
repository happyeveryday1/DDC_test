from socket import *
import time
import json
#################################
# 测试设备的mac
_id = "00124B001EC1050E"
# 网关ip
_ip = "192.168.100.1"
#################################
tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
_times=400


# 上一次RPE的值
lastRPE =0
currentWh = 1
_dict={}
while _times:
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    try:
        _json = json.loads(data)
        #print(_json)
        RPE=int(_json["attributes"]["RPE"])
        #len(dict)，计算字典元素个数，即键的总数。
        _dict[RPE] = 1
        print(RPE,"接收次数",len(_dict))
    except:
        print("ee")

#print(_fials)
#print("丢包率:%.2f %%"%(100*float(_success)/(_success+_fials)))
#print("丢包率:%.2f %%"%(100*float(len(_dict))/400))
