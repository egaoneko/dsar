# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

class List:
	'''List Class.

	This list class is interface for List'''

	def add(self):
		raise NotImplementedError

	def get(self):
		raise NotImplementedError

	def remove(self):
		raise NotImplementedError
		
	def __len__(self):
		raise NotImplementedError

	def toArray(self):
		raise NotImplementedError
