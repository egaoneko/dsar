__author__ = 'jeonjiseong'


def insertion(data_list):
    for i in range(1, len(data_list)):
        key = data_list[i]
        j = i - 1
        while j > -1 and data_list[j] > key:
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = key


if __name__ == "__main__":
    a = [3,1,2,6,7,4,9,8,0,5]
    insertion(a)
    print(a)

'''
    __author__ = 'jeonjiseong'

def make_numbers(mode):

    if mode == "rand":
        file_inst = open("texts/rand.txt", 'w')
        for i in range(0, 100000000):
            file_inst.write(str(randint(0, 100000000))+"\n")
    elif mode == "seq":
        file_inst = open("texts/seq.txt", 'w')
        for i in range(0, 100000000):
            file_inst.write(str(i)+"\n")
    elif mode == "inv":
        file_inst = open("texts/inv.txt", 'w')
        for i in range(99999999, -1, -1):
            file_inst.write(str(i)+"\n")
    else:
        print("wrong input")
    file_inst.close()

    #make_numbers("rand")
    #make_numbers("seq")
    #make_numbers("inv")
    #data_set = [line.strip() for line in open("texts/rand.txt", 'r')]
'''