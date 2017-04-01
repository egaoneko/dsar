import time
import random
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


class SearchAlgo:
    def __init__(self):
        self.frequency = []

    def seq_bin_search(self, data_list, target):
        if self.frequency is not None:
            for i in self.frequency:       # check data in frequency list with linear search
                if i == target:
                    self.frequency.remove(i)        # if target is found, move to first position of list
                    self.frequency.insert(0,i)
                    if len(self.frequency) > (len(data_list) * 0.1):      # if size of frequency list is bigger than 10% of total size of data list
                        self.frequency.pop()
                    print(i)
                    return target

        sorted_data = sorted(data_list)       # sorting data for using binary search
        match = binarysearch(sorted_data, target)             # implement binary search
        if match == "no data":
            print(match)
            return match

        self.frequency.append(match)        # add data in list of frequency
        print(match)
        return match


if __name__ == "__main__":
    dd = range(100000000)
    random.shuffle(dd)      # 81 seconds

    a = SearchAlgo()

    start_time = time.time()
    a.seq_bin_search(dd,3)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    a.seq_bin_search(dd,1143422)
    print("--- %s seconds ---" % (time.time() - start_time))

    k = random.randint(1,100000000)
    start_time = time.time()
    a.seq_bin_search(dd,k)
    print("--- %s seconds ---" % (time.time() - start_time))

    print(a.frequency)      # print list of frequency

    start_time = time.time()
    a.seq_bin_search(dd,3)
    print("--- %s seconds ---" % (time.time() - start_time))
    '''
    a.seq_bin_search(dd,1143422)
    a.seq_bin_search(dd,k)
    a.seq_bin_search(dd,41123)
    a.seq_bin_search(dd,41123)
    print(a.frequency)
    start_time = time.time()
    a.seq_bin_search(dd,41123)
    print("--- %s seconds ---" % (time.time() - start_time))
    #print(a.frequency)
    '''
