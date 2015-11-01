__author__ = 'jeonjiseong'

import sys

r1 = lambda : sys.stdin.readline()
n = int(r1())
input = list()

for i in range(n*3):
        input.append(str(r1()))

templist = [input[i:i+3] for i in range(0,len(input),3)]

def drawrect(lists):
    curlist = lists
    for x in xrange(curlist.__len__()):
        curlist[x]=curlist[x].split()

    value = ''

    temp = curlist[0][0]

    l = list()
    for x in xrange(curlist.__len__()):
        l.append(curlist[x][0])

    k = [[x,l.count(x)] for x in set(l)]

    for x in xrange(k.__len__()):
        if int(k[x][0]) < 1 or int(k[x][0]) > 1000:
            value = "wrong Input"
            return value
        if k[x][1] is 1:
            temp = k[x][0]

    value += temp
    value += ' '

    l = list()
    for x in xrange(curlist.__len__()):
        l.append(curlist[x][1])

    k = [[x,l.count(x)] for x in set(l)]

    for x in xrange(k.__len__()):
        if int(k[x][0]) < 1 or int(k[x][0]) > 1000:
            value = "wrong Input"
            return value
        if k[x][1] is 1:
            temp = k[x][0]

    value+=temp

    return value

for x in xrange(n):
    print drawrect(templist[x])
