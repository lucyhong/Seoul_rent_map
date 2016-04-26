#-*- coding: utf-8 -*-

import json
import requests

# 역정보 모아둔 json 파일을 data 불러옴
with open('station_info.json') as data_file:
	data = json.load(data_file)

# 역 ad_id만 모은 리스트를 만들기 위해 빈 리스트 생성
station_list=[]

# data를 돌면서 ad_id만 station_list에 추가
for x in data:
	station_list.append(x['ad_id'])
	# print (x['ad_id'])

# 생성된 리스트 확인
print (station_list)

# 리스트 요소 갯수 확인
# print (len(station_list))
# 전국 지하철역 갯수가 800개 가까이 되는구나 +ㅁ+ 검색해보니 실제 그러함!