__author__ = 'jeonjiseong'

import sys

def hotsummer(stringlist):
    total = int(stringlist[0])
    used = stringlist[1].split()

    if used.__len__() is not 9 :
        return "Wrong input"

    cal = 0
    for x in used:
        cal += int(x)

    if total >= cal:
        result = "YES"
    else:
        result = "NO"

    return result

if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 1000 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n*2):
        input.append(str(r1()))

    templist = [input[i:i+2] for i in range(0,len(input),2)]

    for x in xrange(templist.__len__()):
        print hotsummer(templist[x])