#-*- coding: utf-8 -*-

# https://api.zigbang.com/v1/search/subway?q=
# https://api.zigbang.com/v2/items/ad/98?radius=1
# https://api.zigbang.com/v1/items?item_ids=4324471

import json
import requests

# 지하철 역정보 가져오기
r = requests.get('https://api.zigbang.com/v1/search/subway?q=')

# 가져온 역정보 json으로 저장하기
with open('station_info.json','w') as outfile:
	json.dump(r.json(),outfile)