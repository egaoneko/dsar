__author__ = 'jeonjiseong'

from copy import deepcopy

def swap(dataset,a,b):
    temp = deepcopy(dataset[a])
    dataset[a] = deepcopy(dataset[b])
    dataset[b] = deepcopy(temp)

def partition(dataset,left,right):
    datalist = dataset
    first = left
    pivot = datalist[first]

    left += 1

    while left <= right:
        while datalist[left] <= pivot and left < right:
            left += 1

        while datalist[right] >= pivot and left <= right:
            right -= 1

        if left < right:
            swap(datalist,left,right)
        else:
            break

    swap(datalist,first, right)
    return right

def quicksort(dataset, left, right):
    datalist = dataset
    if left < right:
        index = partition(datalist,left,right)
        quicksort(datalist,left,index-1)
        quicksort(datalist,index+1,right)

    return datalist

if __name__ == "__main__":
    dataset = [6,4,2,3,1,5]

    sortedarray = quicksort(dataset,0,dataset.__len__()-1)

    print "Sorted array"
    for i in sortedarray:
        print i,