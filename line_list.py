#-*- coding: utf-8 -*-

# 본 파일에서 하고자 하는 것은 select_line.py 에서 호선 고를 때 line_number로 어떻게 넣어야 할지 목록을 만들고자 함

import json

with open('station_info.json') as data_file:
	data = json.load(data_file)

list=[]
line_list = []

# 모든 'short_name' 돌면서 리스트에 추가
for i in data:
    list.append(i['lines'][0]['short_name'])

# unique한 값으로 정리
[line_list.append(x) for x in list if x not in line_list]

# 가나다순으로 정렬
line_list.sort()

print (line_list)
