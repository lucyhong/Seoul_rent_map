# Seoul_rent_map
수도권의 지하철역 근처의 원룸, 오피스텔등의 월세 가격을 알아보는 패키지를 만들고 있습니다.

#### create_station_list.py
* station_info.json 파일에서 데이터를 불러와 돌면서 역의 ad_id만 모은 리스트를 생성함
  * ad_id란 역의 고유한 id를 의미
  * 역 정보(station_info.json)가 다운로드 되어 있는 경우에 사용 가능
  
#### line2.py
* 2호선의 ad_id와 역이름을 추출하여 리스트 생성
  * 호선별 역 ad_id 만 뽑을 수 있도록 만듬
  * 예시로 2호선 추출

#### line_index.py
* select_line.py에서 호선을 선택하여 넣을 때 입력값으로 활용하기 위한 index

#### list_calculation.py
* 리스트 내에 있는 값의 평균값을 계산
  * 역별로 보증금과 월세가격을 리스트로 생성하기 때문에 리스트 연산 필요
  
#### list_comprehension_exercise.py
* for문을 list comprehension 으로 바꾸는 연습
  * for문을 작성하는 대신 list comprehension을 사용할 것을 권장

#### price_crawl.py
* 가장 메인이 되는 function 들이 모여있는 파일
* 방의 정보 중 보증금과 월세에 방의 크리를 추가로 모집하는 모듈 추가
  * get_bang_info
  
#### select_line.py
* 원하는 호선의 short_name을 넣어 해당 호선의 리스트를 생성할 수 있음
  * 역 정보(station_info.json)가 다운로드 되어 있는 경우에 사용 가능
  
#### station_json.py
* 전국 지하철 역들의 정보를 모두 가져와서 json으로 저장

### Data source
* [직방] (https://zigbang.com/)
* 데이터 크롤링을 위해 활용한 URL 3개
 * 지하철 역정보: https://api.zigbang.com/v1/search/subway?q=
 * 지하철 역근처 방 리스트: https://api.zigbang.com/v2/items/ad/98?radius=1
 * 방의 세부정보: https://api.zigbang.com/v1/items?item_ids=4324471

###### 이 프로젝트는 [Berlin rent map](http://www.citylab.com/housing/2016/01/a-station-by-station-subway-map-of-berlin-rents/423102/)에서 영감을 얻었습니다.
