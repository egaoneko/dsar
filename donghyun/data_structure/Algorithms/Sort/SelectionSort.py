# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


def SelectSort(list):
    n = len(list)

    for i in range(0, n - 1):
        maxIdx = i

        for j in range(i + 1, n):
            if list[j] < list[maxIdx]:
                maxIdx = j

            list[i], list[maxIdx] = list[maxIdx], list[i]


if __name__ == '__main__':
    l = [3, 2, 4, 1]

    SelectSort(l)

    print(l)
