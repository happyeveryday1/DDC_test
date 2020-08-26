
import json
a=["{'SW1': 'ON','SCE':1}","{'SW1': 'OFF','SCE':2}"]
# print(type(a[0]))


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json_a='{"SW1": "ON","SCE":1}'
print(json_str)
print(type(json_str))
print(type(json_a))
r=json.loads(json_str)
r2=json.loads(json_a)
print(r)
print(r2)
print(type(r))