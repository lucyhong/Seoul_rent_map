#-*- coding: utf-8 -*-
# 예를 들어 2호선만 뽑아서 리스트를 만들고 싶다.

import json

with open('station_info.json') as data_file:
	data = json.load(data_file)

line_ids=[]
line_names=[]

for i in data:
	if (i['lines'][0]['short_name']) == '2':
		line_ids.append(i['ad_id'])
		line_names.append(i['name'])
	else:
		pass
	shortname = i['lines'][0]['short_name']
	if( '2' in shortname & '부산' not in shortname):

for i in data:
	if (len(i['lines'])) >= 2:
		if (i['lines'][1]['short_name']) == '2':
			line_ids.append(i['ad_id'])
			line_names.append(i['name'])
		else:
			pass
	else:
		pass

# 역의 ad_id 모음 리스트
print (line_ids)

# 역의 이름 모음 리스트
print (line_names)

# 역의 갯수를 확인하기 위해 리스트의 길이 프린트
print (len(line_ids))
