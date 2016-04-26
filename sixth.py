#-*- coding: utf-8 -*-

import json
import requests

# station 많이 돌 필요 없이 테스트를 위해 일단 만들
station_list = [601, 175, 171]

def get_room_list(station_id):
	# 방 정보 넣을 리스트 생성
	room_list=[]
	r = requests.get('https://api.zigbang.com/v2/items/ad/%s?radius=1'%station_id)
	f = r.json()
	for i in f['list_items']:
		i.get('simple_item')
		room_list.append(i.get('simple_item'))
	return room_list

def get_filtered_list(room_list):
	# None값 제외한 최종 방 리스트 만들기
	room_list_final=[]
	filtered = list(filter(None, room_list))
	for i in filtered:
		i.get('item_id')
		room_list_final.append(i.get('item_id'))
	return room_list_final

def get_deposit_rent(room_list_final):
	deposit_list=[]
	rent_list=[]
	for i in room_list_final[:5]: # 너무 많이 가져오면 직방이 놀라니까 일단 다섯개만!
		url = requests.get('https://api.zigbang.com/v1/items?item_ids=%s'%i)
		info = url.json()
		depo = info['items'][0]['item']['deposit']
		deposit_list.append(depo)
		rent = info['items'][0]['item']['rent']
		rent_list.append(rent)
	return deposit_list, rent_list

final_set={}
for station_id in station_list:
	room_list = get_room_list(station_id)
	print (station_id)
	room_list_final = get_filtered_list(room_list)
	deposit_list, rent_list = get_deposit_rent(room_list_final)
	station_set = {"deposit": deposit_list, "rent": rent_list }
	final_set[station_id] = station_set
	
print (final_set)