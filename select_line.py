#-*- coding: utf-8 -*-

import json

with open('station_info.json') as data_file:
	data = json.load(data_file)

def get_station_ids(line_number):
	# line_number에 원하는 호선의 short_name을 넣으면 해당역 리스트 생성
	line_ids=[]
	line_names=[]
	for i in data:
		for j in range(len(i['lines'])):
			if (i['lines'][j]['short_name']) == line_number:
				line_ids.append(i['ad_id'])
				line_names.append(i['name'])
			else:
				pass
	return line_ids, line_names


if __name__=='__main__':

	# '2' 자리에 원하는 호선 숫자를 넣으면 됩니다.
	line_ids, line_names = get_station_ids('2')
	print (line_ids)
	print (line_names)
	print (len(line_ids))