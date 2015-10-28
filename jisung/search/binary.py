__author__ = 'jeonjiseong'

def binarysearch(datalist,target):
    size = len(datalist)
    left = 0
    right = size - 1

    while left <= right:
        mid = (left+right) / 2
        if target == datalist[mid][1]:
            return datalist[mid]
        elif target > datalist[mid][1]:
            left = mid +1
        else:
            right = mid -1
    return None

def getkey(item):
    return item[1]

if __name__ == "__main__":
    list = [(1,877.88),(2,176.23),(3,365.92),(4,433.42),(5,323.23),(6,233.11),(7,456.23),(8,966.44),(9,342.64),(10,133.32)]

    sortedlist = sorted(list,key=getkey)

    found = binarysearch(sortedlist,433.42)
    print found