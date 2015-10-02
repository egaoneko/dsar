__author__ = 'jeonjiseong'

import sys

def encrypt(stringarray):
    stringarray = stringarray.rstrip()

    if len(stringarray) > 100:
        return "your text too long"

    stringarray = stringarray.rstrip()
    midlist = list(stringarray)
    templist = list()

    for x in range(0,stringarray.__len__(),2):
        templist.append(midlist[x])

    for x in range(1,stringarray.__len__(),2):
        templist.append(midlist[x])

    resultstr = ''.join(templist)

    return resultstr


if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 10 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print encrypt(input[x])