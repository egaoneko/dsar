__author__ = 'jeonjiseong'

import sys

def bracket(stringline):
    if len(stringline) > 10000 :
        return "Too long"

    bracketlist = list(stringline.rstrip())

    bracketdict = {"(":")","[":"]","{":"}"}
    stacklist = list()

    for i in xrange(len(bracketlist)):
        if len(stacklist) == 0:
            stacklist.append(bracketlist[i])
            continue

        if i == len(bracketlist):
            break

        if bracketlist[i] == bracketdict.get(stacklist[len(stacklist)-1]):  #Use method like stack
            stacklist.pop()
        else:
            stacklist.append(bracketlist[i])

    if len(stacklist) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 100 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print bracket(input[x])