# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


def InsertionSort(list):
    n = len(list)

    for i in range(1, n):
        insData = list[i]

        j = i - 1
        while j >= 0:
            if list[j] > insData:
                list[j + 1] = list[j]
                j -= 1
            else:
                break

        list[j + 1] = insData


if __name__ == '__main__':
    l = [5, 3, 2, 4, 1]

    InsertionSort(l)

    print(l)
