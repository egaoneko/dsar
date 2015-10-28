__author__ = 'jeonjiseong'

import sys

def fixparen(stringline):
    stringline = stringline.rstrip()
    stringlist = stringline.split()

    if len(stringlist[0]) > 100:
        return "First string is too long"
    if len(stringlist[1]) != 4:
        return "The length of second string is always 4"

    firstlist = list(stringlist[0])
    secondlist = list(stringlist[1])

    priority = dict()
    pairdict = {"(":")","[":"]","{":"}","<":">",")":"(","]":"[","}":"{",">":"<"}
    stacklist = list()
    openlist = ("(","{","[","<")
    closelist = (")","}","]",">")

    for i in xrange(len(secondlist)):
        priority[secondlist[i]] = i

    tmplist = firstlist
    for i in xrange(len(tmplist)):
        factor = tmplist[i]
        if factor in openlist:
            stacklist.append((i,factor))
        elif factor in closelist:
            closebrat = factor
            openbrat = pairdict.get(closebrat)
            preopenbratlist = stacklist.pop()
            rankopen = priority.get(openbrat)
            rankpreopen = priority.get(preopenbratlist[1])

            if rankopen < rankpreopen :
                firstlist[preopenbratlist[0]]=openbrat
            elif rankopen == rankpreopen:
                continue
            else:
                firstlist[i]=pairdict.get(preopenbratlist[1])

    returnstring = ''.join(firstlist)
    return returnstring

if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print fixparen(input[x])