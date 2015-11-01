# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'

import Queue


def RadixSort(l):
    buckets = list()
    maxLen = len(str(max(l)))
    divfac = 1

    # Init Buckets
    for i in range(10):
        buckets.append(Queue.Queue())

    # Longest data length
    for pos in range(maxLen):

        # roop by length of list
        for di in range(len(l)):
            # get radix
            radix = int(l[di] / divfac) % 10

            # input data by using radix
            buckets[radix].enQueue(l[di])

        di = 0
        for bi in range(10):
            while len(buckets[bi]) > 0:
                l[di] = buckets[bi].deQueue()
                di += 1

        divfac *= 10


if __name__ == '__main__':
    l = [13, 212, 14, 7141, 10987, 6, 15]

    RadixSort(l)
    print(l)
