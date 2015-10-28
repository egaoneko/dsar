# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Iterator
import LinkedList

class Queue:
	'''Queue Class.

	This queue class is uesd for storing datas.
	And this class is consist of link.'''

	def __init__(self):
		self.__list__ = LinkedList.LinkedList()
		
	def isEmpty(self):
		if len(self.__list__) == 0:
			return True
		else:
			return False

	def enQueue(self, data):
		self.__list__.linkLast(data)

	def deQueue(self):
		data = self.peek()
		self.__list__.unlinkFirst()
		return data

	def peek(self):
		if self.isEmpty():
			raise EmptyError

		return self.__list__.getFirst()

	def __len__(self):
		return len(self.__list__)

	def toArray(self):
		return self.__list__.toArray()

if __name__ == '__main__':
	queue = Queue()
	queue.enQueue(1)
	queue.enQueue(2)
	queue.enQueue(3)
	queue.enQueue(4)
	queue.enQueue(5)

	print(queue.peek())
	print(queue.deQueue())


	iterator = Iterator.Iterator(queue)
	
	while iterator.hasNext():
		print(iterator.next())
