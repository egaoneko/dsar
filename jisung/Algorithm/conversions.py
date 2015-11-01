#__author__ = 'jeonjiseong'

from __future__ import division
import sys

def convert(string,index):
    string = string.rstrip()

    stringlist = string.split()

    number = float(stringlist[0])

    measurment = stringlist[1]

    if measurment == "kg":
        mid = number * 2.2046
        result = "{0:.4f}".format(round(mid,4))
        chmean = "lb"
    elif measurment == "lb":
        mid = number * 0.4536
        result = "{0:.4f}".format(round(mid,4))
        chmean = "kg"
    elif measurment == "l":
        mid = number * 0.2642
        result = "{0:.4f}".format(round(mid,4))
        chmean = "g"
    elif measurment == "g":
        mid = number * 3.7854
        result = "{0:.4f}".format(round(mid,4))
        chmean = "l"
    else:
        result = "Wrong Measurment"

    return str(index+1) + " " +result + " " +chmean

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
        print convert(input[x],x)


'''
5
1 kg
2 l
7 lb
3.5 g
0 l
'''