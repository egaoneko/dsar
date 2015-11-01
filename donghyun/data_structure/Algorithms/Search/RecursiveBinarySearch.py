# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


def search(list, first, last, target):
    if first > last:
        return -1

    mid = (first + last) / 2

    if list[mid] == target:
        return mid
    elif target < list[mid]:
        return search(list, first, mid - 1, target)
    else:
        return search(list, mid + 1, last, target)


if __name__ == '__main__':
    l = [1, 3, 6, 9, 11, 15, 20]

    print(search(l, 0, len(l) - 1, 6))
