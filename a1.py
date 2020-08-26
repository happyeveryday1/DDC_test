from socket import *
import time
import json


#################################
# 测试设备的mac
_id = "00124B001D13354D"
# 网关ip
_ip = "192.168.1.194"
#################################

tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))
_times=409
list_data=[]
d2=[]
d3=[]
list_data2=[]
list_len=[]
#_success = 0
_dict_RPE={}
_dict={}
t=0
#action_times=0
while _times:
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    try:

        _json = json.loads(data)
        list_data.append(_json)
        print(list_data)
        for item in list_data:
            if item["attributes"]["RPE"] not in d2:
                d2.append(item["attributes"]["RPE"])
                #d3.append(item["attributes"]["RPE"])
                print(d2)
                d3.append(item["attributes"]["RPE"])
                print(len(d3))

            print('去重后列表长度：%d' % len(d3))
            print(d3)
    except:
        print("eee")


#print(_fials)
#print("丢包率:%.2f %%"%(100*float(_success)/(_success+_fials)))
#print("丢包率:%.2f %%"%(100*float(len(_dict))/400))
