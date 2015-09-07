# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Iterator
import List

class ArrayList(List.List):
	'''Array List Class.

	This array list class is uesd for storing datas.
	And this class is consist of array.'''

	def __init__(self):
		self.__array__ = []
	
	def add(self, data):
		self.__array__.append(data)

	def get(self, index):
		return self.__array__[index]

	def remove(self, index):
		size = len(self.__array__)

		if len(self.__array__) == 0:
			raise NotExistedData

		if index < 0 or index > size:
			raise IndexError
		elif index == size:
			return self.__array__.pop()
		else:
			ret = self.get(index)
			self.__array__ = self.__array__[:index]+self.__array__[index+1:]
			return ret
		
	def __len__(self):
		return len(self.__array__)

	def toArray(self):
		return self.__array__

if __name__ == '__main__':
	list = ArrayList()
	list.add(1)
	list.add(2)
	list.add(3)
	list.add(4)
	list.add(5)
	list.add(6)

	print(len(list))

	list.get(3)
	list.remove(3)
	#list.remove(7)
	list.get(3)

	iterator = Iterator.Iterator(list)
	
	while iterator.hasNext():
		print(iterator.next())
