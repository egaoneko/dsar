# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

def BubbleSort(list):

	n = len(list)

	for i in range(0, n-1):
		for j in range(0, n-i-1):
			if list[j] > list[j+1] :
				list[j], list[j+1] = list[j+1], list[j]

if __name__ == '__main__':
	l = [3, 2, 4, 1]

	BubbleSort(l)

	print(l)
