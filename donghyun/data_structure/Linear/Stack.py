# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Iterator
import LinkedList

class Stack:
	'''Stack Class.

	This stack class is uesd for storing datas.
	And this class is consist of link.'''

	def __init__(self):
		self.__list__ = LinkedList.LinkedList()
		
	def isEmpty(self):
		if len(self.__list__) == 0:
			return True
		else:
			return False

	def push(self, data):
		self.__list__.linkLast(data)

	def pop(self):
		data = self.peek()
		self.__list__.unlinkLast()
		return data

	def peek(self):
		if self.isEmpty():
			raise EmptyError

		return self.__list__.getLast()

	def __len__(self):
		return len(self.__list__)

	def toArray(self):
		return self.__list__.toArray()

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)

	print(stack.peek())
	print(stack.pop())


	iterator = Iterator.Iterator(stack)
	
	while iterator.hasNext():
		print(iterator.next())
