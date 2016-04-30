#-*- coding: utf-8 -*-
import re
import json
import requests

from lxml import html

BASEURL = 'https://api.zigbang.com'
ITEM_URL = "https://www.zigbang.com/items/{}"

def get_room_list(station_id):
    # 방 정보 넣을 리스트 생성
    r = requests.get('%s/v2/items/ad/%s?radius=1' % (BASEURL, station_id)).json()
    return [i.get('simple_item') for i in r['list_items'] if 'simple_item' in i.keys()]

def get_deposit_rent(room_list, limit=None):
    deposit_list, rent_list = [], []
    for i in room_list[:limit]:
        r = requests.get('%s/v1/items?item_ids=%s' % (BASEURL, i)).json()
        deposit_list.append(r['items'][0]['item']['deposit'])
        rent_list.append(r['items'][0]['item']['rent'])
    return deposit_list, rent_list
    
def get_bang_info(item_number): # one of room_list item, ex) '3035158' not working now its old item number
    data = requests.get(ITEM_URL.format(item_number))
    content = html.fromstring(data.text)
    deposit = content.cssselect('em')[0].text_content()
    fee = content.cssselect('em')[1].text_content()
    #parsing part of room square
    p = content.cssselect('tr td')[6].text_content().strip()
    sqr = re.findall(r'\d+P', content.cssselect('tr td')[6].text_content().strip())[0][:-1]
    return int(deposit), int(fee), int(sqr)

if __name__=='__main__':
    station_list = [601, 175, 171] # station 많이 돌 필요 없이 테스트를 위해 일단 만들

    final_set = {}
    for station_id in station_list:
        print(station_id)
        room_list = get_room_list(station_id)
        deposit_list, rent_list = get_deposit_rent(room_list, limit=5)
        
        size_list = [] #리스트자꾸 만드는건 별로 좋은건 아니라고 하네요.
        for item_number in room_list: #속도가 느려질 가능성이 매우 큼.
            d, f, p = get_bang_info(item_number) #상세 페이지에서 만약에 size가 없는경우 순서가 바뀌어 버릴수가 있습니다.
            size_list.append(p) 
            
        final_set[station_id] = {"deposit": deposit_list, "rent": rent_list, "size" : size_list}
        
    print(final_set)
