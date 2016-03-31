import time
import random
from jisung.sort import bubble2, insertion, merge, quick2
import sys

sys.setrecursionlimit(100000000)
if __name__ == "__main__":

    a = range(100000000)
    #random.shuffle(a)
    #a.reverse()

    start_time = time.time()
    insertion.insertion(a)
    #merge.mergesort(a)
    #bubble2.bubbleSort(a)
    #quick2.quickSort(a)
    print("--- %s seconds ---" % (time.time() - start_time))

