#-*- coding: utf-8 -*-

# 보증금 및 월세 평균을 구하기 위해 리스트 내 값들의 연산 코드 작성

list_example = [10, 20, 40, 100]

def get_list_average(list):
	# 리스트 내에 있는 값들의 평균을 구함
	sum = 0
	for i in list:
		sum += i
	average = (sum / len(list))
	return average

average = get_list_average(list_example)

print (average)