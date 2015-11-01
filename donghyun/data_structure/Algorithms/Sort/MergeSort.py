# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


def merge(list, lo, mid, hi):
    tmp = list[:]

    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            list[k] = tmp[j]
            j += 1
        elif j > hi:
            list[k] = tmp[i]
            i += 1
        elif tmp[j] < tmp[i]:
            list[k] = tmp[j]
            j += 1
        else:
            list[k] = tmp[i]
            i += 1


def sort(list, lo, hi):
    if hi <= lo: return
    mid = lo + int((hi - lo) / 2)
    sort(list, lo, mid)
    sort(list, mid + 1, hi)
    merge(list, lo, mid, hi)


def MergeSort(list):
    sort(list, 0, len(list) - 1)


if __name__ == '__main__':
    l = [3, 2, 4, 1, 7, 6, 5]

    MergeSort(l)
    print(l)
