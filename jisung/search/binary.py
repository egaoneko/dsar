__author__ = 'jeonjiseong'


def binarysearch(datalist, target):
    size = len(datalist)
    left = 0
    right = size - 1

    while left <= right:
        mid = (left+right) / 2
        if target == datalist[mid]:
            return datalist[mid]
        elif target > datalist[mid]:
            left = mid +1
        else:
            right = mid -1
    return "no data"

if __name__ == "__main__":

    alist = [1,2,3,4,5,6,7,8,9,10,11]
    #sortedlist = sorted(alist)

    found = binarysearch(alist, 12)
    print found