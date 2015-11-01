# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Heap


class PQueue(Heap.Heap):
    '''Priority Queue Class.

    This pqueue class is used for priority queue.
    And this class is consist of heap.'''

    def __init__(self, pc):
        # super().__init__(self, pc)
        super(PQueue, self).__init__(pc)

    def isEmpty(self):
        # return super().isEmpty(self)
        return super(PQueue, self).isEmpty()

    def pQPush(self, data):
        # super().heapPush(self,data)
        super(PQueue, self).heapPush(data)

    def pQPop(self):
        # return super().headPop(self)
        return super(PQueue, self).headPop()


if __name__ == '__main__':

    pc = lambda x, y: x - y

    pq = PQueue(pc)
    pq.__array__ = [0, 74, 71, 64, 63, 56, 33, 50, 30, 10, 11]
    pq.__size__ = 10
    pq.pQPush(22)
    pq.pQPush(73)
    pq.pQPush(76)

    print(pq.__array__)

    while pq.isEmpty() != True:
        print(pq.__array__)
        print(pq.pQPop())
