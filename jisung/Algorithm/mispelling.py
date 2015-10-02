__author__ = 'jeonjiseong'

import sys

'''
r1 = lambda : sys.stdin.readline()

n = int(r1())

input = list()

for i in range(n):
    str = r1().split()
    input.append((int(str[0]),str[1]))
    print str
    print input

def mispell(input):
    print [str[:mis-1]+str[mis:] for mis,str in input]
    return [str[:mis-1]+str[mis:] for mis,str in input]

for idx, str in enumerate(mispell(input)):
    print("%d %s" % (idx+1, str))
'''
def mispell(stringarray,index):
    stringarray = stringarray.rstrip()

    templist = stringarray.split()

    number = int(templist[0])
    string = templist[1]

    if len(string) > 80:
        return "your text too long"

    if number > len(string) or number < 1:
        return "wrong number"

    midarray = list(string)

    midarray.pop(number-1)

    resultarr = "".join(midarray)
    indexnum = str(index+1)
    resultarr = indexnum + " " + resultarr

    return resultarr

if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 1000 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print mispell(input[x],x)
'''
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON
'''