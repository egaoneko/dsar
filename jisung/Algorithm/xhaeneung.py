__author__ = 'jeonjiseong'

import sys

def xhaeneung(stringarray):
    arraylist = stringarray.split()
    result = arraylist[4]
    result = result.lower()

    if len(result) > 10:
        return "result is too length"

    numdict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}

    a = numdict.get(arraylist[0])
    b = numdict.get(arraylist[2])

    if a > 10 or a < 0 :
        return "Wrong input"

    if b > 10 or b < 0 :
        return "Wrong input"

    if arraylist[1] is "+":
        res = a + b
    elif arraylist[1] is "-":
        res = a - b
    elif arraylist[1] is "*":
        res = a * b
    else:
        return "Wrong Operator"

    if res > 10 or res < 0:
        return "No"

    for eng,num in numdict.items():
        if num == res:
            c = eng

    sores1 = sorted(c)
    sores2 = sorted(result.rstrip())

    if len(sores1) is not len(sores2):
        return "No"
    else:
        if sores1 != sores2:
            return "No"

    return "Yes"

if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print xhaeneung(input[x])