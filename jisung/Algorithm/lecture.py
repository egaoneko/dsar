__author__ = 'jeonjiseong'

import sys

r1 = lambda : sys.stdin.readline()
n = int(r1())
input = list()

for i in range(n):
        input.append(str(r1()))

def lecture(stringarray):
    stringarray = stringarray.lower()
    stringarray = stringarray.rstrip()
    lenstr =  stringarray.__len__()

    if lenstr > 1000:
        return 'Out of length'
    if lenstr%2 is not 0:
        return 'Not odd number'
    #aaa
    #alpha = list('abcdefghijklmnopqrstuvwxyz')
    #dictlist = {}
    #i=1
    #for x in alpha:
    #    dictlist[x] = i
    #    i+=1

    l = list(stringarray)

    tempstr = list()

    for x in range(0,l.__len__(),2):
        a = l[x] + l[x+1]
        tempstr.append(a)

    #c=list()
    #for x in tempstr:
    #    b = list()
    #    a = list(x)
    #    b.append(int(dictlist[a[0]]))
    #    b.append(int(dictlist[a[1]]))
    #    c.append([x,b])

    valist = ''

    for x in sorted(tempstr):
        valist += x

    return valist

    #print tempstr
    #print tempdict

for x in xrange(input.__len__()):
    print lecture(input[x])
