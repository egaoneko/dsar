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

    pc = lambda x, y: y - x

    pq = PQueue(pc)
    pq.pQPush(6)
    pq.pQPush(2)
    pq.pQPush(7)
    pq.pQPush(9)
    pq.pQPush(11)
    pq.pQPush(1)
    pq.pQPush(3)
    pq.pQPush(16)
    pq.pQPush(12)

    while pq.isEmpty() != True:
        print(pq.__array__)
        print(pq.pQPop())
