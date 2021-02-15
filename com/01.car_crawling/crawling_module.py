# -*- coding:utf-8 -*-
# 패키지 임포트
import json
import requests
import re
from bs4 import BeautifulSoup


# 크롤링 주소 설정 함수
def url(obj_url):
    req = requests.get(obj_url)
    html = req.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# 대분류 설정(차량 이름이 있는 리스트만 추출)
def find_list(obj , tag, option):
    model_list = obj.find(tag, option)
    return model_list

# 리스트에서 차 이름 찾기, 리스트 생성
def find_car(obj, tag, option):
    carName_find = obj.find_all(tag, option)
    car_list = []

    for i in carName_find:

        carName = re.sub('[^a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣 ]','',i.text)

        temp = {}
        temp = carName

        car_list.append(temp)

    return car_list

# json 형식으로 가공 및 저장
def save_json(co_name,list_obj):

    result = {}
    json_data = None
    result[co_name] = list_obj

    result_json = json.dumps(result, ensure_ascii=False)

    # 제이슨 파일이 있다면 읽어오기, 없을 경우 파일 생성
    try:
        with open('car_list.json', 'r', encoding='utf-8') as read_list:
            json_data = json.load(read_list)

    except:
        with open('car_list.json', 'w', encoding='utf-8') as new_list:
            new_list.write(result_json)

    if json_data is not None:

        json_data[co_name] = list_obj
        with open('car_list.json', 'w', encoding='utf-8') as add_list:
            json.dump(json_data, add_list, ensure_ascii=False)
