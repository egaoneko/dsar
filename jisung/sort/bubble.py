__author__ = 'jeonjiseong'

def bubblesort(dataset, len):
    for i in xrange(len-1):
        for j in xrange(len-(i+1)):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j+1]
                dataset[j+1] = dataset[j]
                dataset[j] = temp
            #else:
            #   break

    return dataset

# improvement = change the code that exit the loop if inserted data is sorted

if __name__ == "__main__":
    data = [6,4,2,3,1,5]
    #data = [1,2,3,4,5,6]
    bubblesort(data, data.__len__())
    print(data)
