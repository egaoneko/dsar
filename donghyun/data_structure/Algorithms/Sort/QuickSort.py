# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


def getMid(list, lo, hi):
    # Bubble Sort
    mi = lo + int((hi - lo) / 2)

    if list[lo] > list[mi]:
        lo, mi = mi, lo

    if list[mi] > list[hi]:
        mi, hi = hi, mi

    if list[lo] > list[mi]:
        lo, mi = mi, lo

    return mi


def partition(list, lo, hi):
    i = lo + 1
    j = hi

    mi = getMid(list, lo, hi)
    lo, mi = mi, lo

    while True:
        # while list[lo] > list[i]:
        while list[lo] >= list[i]:
            if i == hi: break
            i += 1

        # while list[lo] < list[j]:
        while list[lo] <= list[j]:
            if j == lo: break
            j -= 1

        if i >= j:
            break

        list[i], list[j] = list[j], list[i]

    list[lo], list[j] = list[j], list[lo]
    return j


def QuickSort(list, lo, hi):
    if hi <= lo: return

    pivot = partition(list, lo, hi)
    QuickSort(list, lo, pivot - 1)
    QuickSort(list, pivot + 1, hi)


if __name__ == '__main__':
    # l = [3, 2, 4, 1, 7, 6, 5]
    # l = [3, 3, 3]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    QuickSort(l, 0, len(l) - 1)
    print(l)
