import json

with open('station_info.json') as data_file:
	data = json.load(data_file)

list=[]

# 모든 'short_name' 돌면서 리스트에 추가
# for i in data:
#    list.append(i['lines'][0]['short_name'])

list = [ i['lines'][0]['short_name'] for i in data]

print (list)