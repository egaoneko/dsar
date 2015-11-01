# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


class Iterator:
    def __init__(self, list):
        self.__list__ = list.toArray()
        self.__index__ = 0

    def hasNext(self):
        return self.__index__ < len(self.__list__)

    def next(self):
        ret = self.__list__[self.__index__]
        self.__index__ += 1
        return ret
