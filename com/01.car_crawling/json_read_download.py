from crawling_module import *
import json

with open('car_list.json', 'r', encoding='utf-8') as read_list:
    json_data = json.load(read_list)

# 회사 리스트(Kia, Hyundai etc...)
co_list = list(json_data.keys())

# 데이터 끄내기
for i in co_list:
    for j in json_data[i]:
        print(i+"_"+j)