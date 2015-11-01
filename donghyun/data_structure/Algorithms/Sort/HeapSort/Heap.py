# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


class Heap(object):
    ''' Heap Class.

    This heap class is used for Priority Queue.
    And this class is consist of array.'''

    def __init__(self, pc):
        self.__array__ = list()
        self.__array__.append(0)
        self.__pc__ = pc  # Priority Comp
        self.__size__ = 0

    def isEmpty(self):
        if self.__size__ == 0:
            return True
        else:
            return False

    def getParentIDX(self, idx):
        return idx >> 1

    def getLChildIDX(self, idx):
        return idx << 1

    def getRChildIDX(self, idx):
        return (idx << 1) + 1

    def getHiPriChildIDX(self, idx):
        lChildIDX = self.getLChildIDX(idx)

        if lChildIDX > self.__size__:
            return 0
        elif lChildIDX == self.__size__:
            return lChildIDX
        else:
            rChildIDX = self.getRChildIDX(idx)
            # print((idx, lChildIDX, rChildIDX))
            if self.__pc__(self.__array__[lChildIDX], self.__array__[rChildIDX]) < 0:
                return rChildIDX
            else:
                return lChildIDX

    def heapPush(self, data):
        idx = self.__size__ + 1
        self.__array__.append(0)

        while idx != 1:
            if self.__pc__(data, self.__array__[self.getParentIDX(idx)]) > 0:
                self.__array__[idx] = self.__array__[self.getParentIDX(idx)]
                idx = self.getParentIDX(idx)
            else:
                break

        self.__array__[idx] = data
        self.__size__ += 1

    def heapPop(self):
        if self.__size__ < 1:
            raise EmptyHeapError

        ret = self.__array__[1]
        lastData = self.__array__[self.__size__]

        parentIdx = 1

        childIdx = self.getHiPriChildIDX(parentIdx)
        while childIdx != 0:
            if self.__pc__(lastData, self.__array__[childIdx]) >= 0:
                break

            self.__array__[parentIdx] = self.__array__[childIdx]
            parentIdx = childIdx
            childIdx = self.getHiPriChildIDX(parentIdx)

        self.__array__[parentIdx] = lastData
        self.__size__ -= 1
        self.__array__.pop()
        return ret


if __name__ == '__main__':

    pc = lambda x, y: y - x

    heap = Heap(pc)
    heap.heapPush(6)
    heap.heapPush(3)
    heap.heapPush(7)
    heap.heapPush(10)
    heap.heapPush(12)
    heap.heapPush(14)
    heap.heapPush(1)
    heap.heapPush(4)

    while heap.isEmpty() != True:
        print(heap.__array__)
        print(heap.heapPop())
