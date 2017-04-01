__author__ = 'jeonjiseong'


def mergesort(data_list):
    if len(data_list) > 1:
        mid = len(data_list)//2
        lefthalf = data_list[:mid]
        righthalf = data_list[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                data_list[k] = lefthalf[i]
                i += 1
            else:
                data_list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            data_list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            data_list[k] = righthalf[j]
            j += 1
            k += 1



if __name__ == "__main__":
    a = [3,1,2,6,7,4,9,8,0,5]
    mergesort(a)
    print(a)