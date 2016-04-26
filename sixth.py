#-*- coding: utf-8 -*-

import json
import requests


BASEURL = 'https://api.zigbang.com'


def get_room_list(station_id):
    # 방 정보 넣을 리스트 생성
    r = requests.get('%s/v2/items/ad/%s?radius=1' % (BASEURL, station_id)).json()
    return [i.get('simple_item') for i in r['list_items']]


def filter_room_list(room_list):
    # None값 제외한 최종 방 리스트 만들기
    filtered = list(filter(None, room_list))
    return [i.get('item_id') for i in filtered]


def get_deposit_rent(room_list, limit=None):
    deposit_list, rent_list = [], []
    for i in room_list[:limit]:
        r = requests.get('%s/v1/items?item_ids=%s' % (BASEURL, i)).json()
        deposit_list.append(r['items'][0]['item']['deposit'])
        rent_list.append(r['items'][0]['item']['rent'])
    return deposit_list, rent_list


if __name__=='__main__':
    station_list = [601, 175, 171] # station 많이 돌 필요 없이 테스트를 위해 일단 만들

    final_set = {}
    for station_id in station_list:
        print(station_id)
        room_list = get_room_list(station_id)
        room_list = filter_room_list(room_list)
        deposit_list, rent_list = get_deposit_rent(room_list, limit=5)
        final_set[station_id] = {"deposit": deposit_list, "rent": rent_list }
    print(final_set)
