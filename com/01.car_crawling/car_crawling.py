# -*- coding:utf-8 -*-
# 패키지 임포트
from crawling_module import *

# 기아 자동차
obj = url('https://www.kia.com/kr/main.html')
list_obj = find_list(obj, 'ul', {'class' : 'grid_u'})
json_list = find_car(list_obj, 'strong', {'class' : 'g_name'})
save_json('Kia', json_list)

# 현대 자동차
obj = url('https://www.hyundai.com/kr/ko/e')
list_obj = find_list(obj, 'div', {'class' : 'model_info'})
json_list = find_car(list_obj, 'span', {'class' : 'title'})
save_json('HyunDai', json_list)
