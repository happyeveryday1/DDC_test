import pandas as pd
import time
from time import strftime,localtime
from socket import *
import json
import xlrd
import xlwt
# 测试设备的mac
_id ="00124B002108FFC0"
#_id ="00124B001B581E48"
# 网关ip
_ip = "192.168.1.194"

tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect((_ip, 8888))

df = pd.read_excel("testcase.xls", usecols=[0], names=None,sheet_name='SG-TK6场景')
df_li = df.values.tolist()

result = []
for s_li in df_li:
    result.append(s_li[0])
    #print(result)
for item in result:
    print(item)
time.sleep(3)

for s in result:
    print(s)
    if s != 1:
        time.sleep(1)
        r = json.loads(s)
        #print(r)
        _json_data = {
            "sourceId": "0",
            "requestType": "cmd",
            "serialNum": -1,
            "id": _id,
            "attributes": r
        }
        ret = tcp_client_socket.send(bytes(json.dumps(_json_data).encode('utf-8')))
        data = tcp_client_socket.recv(10240)
        #print(strftime("%Y-%m-%d %H:%M:%S",localtime()),data.decode())
        #result.remove(s)
        #print(result.remove(s))

        result[result.index(s)] = 1
        #print(strftime("%Y-%m-%d %H:%M:%S", localtime()), r)
        time.sleep(2)







