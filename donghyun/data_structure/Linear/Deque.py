# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Iterator
import LinkedList


class Deque:
    '''Deque Class.

    This deque class is uesd for storing datas.
    And this class is consist of link.'''

    def __init__(self):
        self.__list__ = LinkedList.LinkedList()

    def isEmpty(self):
        if len(self.__list__) == 0:
            return True
        else:
            return False

    def addFirst(self, data):
        self.__list__.linkFirst(data)

    def addLast(self, data):
        self.__list__.linkLast(data)

    def removeFirst(self):
        data = self.getFirst()
        self.__list__.unlinkFirst()
        return data

    def removeLast(self):
        data = self.getLast()
        self.__list__.unlinkLast()
        return data

    def getFirst(self):
        if self.isEmpty():
            raise EmptyError

        return self.__list__.getFirst()

    def getLast(self):
        if self.isEmpty():
            raise EmptyError

        return self.__list__.getLast()

    def __len__(self):
        return len(self.__list__)

    def toArray(self):
        return self.__list__.toArray()


if __name__ == '__main__':
    deque = Deque()

    deque.addFirst(1)
    deque.addFirst(2)
    deque.addFirst(3)
    deque.addLast(4)
    deque.addLast(5)

    iterator = Iterator.Iterator(deque)

    while iterator.hasNext():
        print(iterator.next())

    deque.removeFirst()
    deque.removeLast()

    iterator = Iterator.Iterator(deque)

    while iterator.hasNext():
        print(iterator.next())
