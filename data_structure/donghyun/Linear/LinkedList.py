# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Iterator
import List

class Node:
	'''Node Class.'''

	def __init__(self, prev, data, next):
		self.prev = prev
		self.data = data
		self.next = next

class LinkedList(List.List):
	'''Linked List Class.

	This linked list class is uesd for storing datas.
	And this class is consist of link.'''

	def __init__(self):
		self.__head__ = Node(None, None, None)
		self.__tail__ = Node(None, None, None)

		self.__head__.next = self.__tail__
		self.__tail__.prev = self.__head__
		self.__size__ = 0
		
	def linkFirst(self, data):
		newNode = Node(self.__head__, data, self.__head__.next)
		self.__head__.next.prev = newNode
		self.__head__.next = newNode
		
		self.__size__ += 1
		
	def linkLast(self, data):
		newNode = Node(self.__tail__.prev, data, self.__tail__)
		self.__tail__.prev.next = newNode
		self.__tail__.prev = newNode

		self.__size__ += 1
	
	def add(self, data):
		self.linkLast(data)

	def node(self, index):
		if index < (self.__size__  >> 1):
			x = self.__head__.next
			for i in range(index):
				x = x.next
			return x
		else:
			x = self.__tail__.prev
			for i in range(index, 0, -1):
				x = x.prev
			return x

	def get(self, index):
		
		if index < 0 or index > self.__size__-1:
			raise IndexError

		return self.node(index).data

	def unlink(self, node):
		ret = node

		node.prev.next = node.next
		node.next.prev = node.prev

		self.__size__ -= 1
		return node

	def remove(self, index):

		if index < 0 or index > self.__size__ -1:
			raise IndexError

		return self.unlink(self.node(index)).data
		
	def __len__(self):
		return self.__size__

	def toArray(self):
		arr = []
		
		x = self.__head__.next

		while x != None:
			arr.append(x.data)
			x = x.next
	
		return arr

if __name__ == '__main__':
	list = LinkedList()
	list.add(1)
	list.add(2)
	list.add(3)
	list.add(4)
	list.add(5)
	list.add(6)

	list.get(3)
	list.remove(3)
	list.get(3)

	iterator = Iterator.Iterator(list)
	
	while iterator.hasNext():
		print(iterator.next())
