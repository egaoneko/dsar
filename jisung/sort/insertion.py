__author__ = 'jeonjiseong'
'''
def insertionsort(dataset,len):
    datalist = dataset
    for i in range(1,len,1):
        #print "i %d" % i

        for x in range(0,i,1):
            if datalist[i-1] <= datalist[i]:
                break
        #if datalist[i-1] <= datalist[i]:
        #    continue

        #value = datalist[i]
        #print value
        j = 0
        while j < i:
            #print "j %d" % j
            if datalist[j] > datalist[i]:
                temp = datalist[j]
                datalist[j] = datalist[i]
                datalist[i] = temp
                break
            j+=1
            #print j
    return datalist
'''
'''
def insertionsort(dataset,len):
    datalist = dataset

    for i in range(1,len,1):
        pivot = datalist[i]
        for x in xrange(i):
            if datalist[x]

if __name__ == "__main__":
    dataset = [6,4,2,3,1,5]

    sortedarray = insertionsort(dataset,dataset.__len__())

    print "Sorted array"
    for i in sortedarray:
        print i,
'''