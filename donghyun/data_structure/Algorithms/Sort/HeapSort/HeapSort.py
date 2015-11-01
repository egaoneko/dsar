# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Heap


def HeapSort(list, pc):
    heap = Heap.Heap(pc)

    for i in xrange(len(list)):
        heap.heapPush(list[i])

    for i in xrange(len(list)):
        list[i] = heap.heapPop()


if __name__ == '__main__':
    pc = lambda x, y: y - x
    l = [3, 4, 2, 1]

    HeapSort(l, pc)
    print (l)
