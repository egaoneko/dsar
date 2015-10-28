__author__ = 'jeonjiseong'

import sys

def weird(number):
    numberstring = number.rstrip()

    number = int(numberstring)

    if number > 500000 or number < 1:
        return "Error : Out of range"

    proper = list()
    for i in xrange(number):
        if i == 0:
            continue
        if number%i == 0:
            proper.append(i)

    sumset = sum(proper)

    #weirdnum = [70, 836, 4030, 5830, 7192, 7912, 9272, 10430, 10570, 10792, 10990, 11410, 11690, 12110, 12530, 12670, 13370, 13510, 13790, 13930, 14770, 15610, 15890, 16030, 16310, 16730, 16870, 17272, 17570, 17990, 18410, 18830, 18970, 19390, 19670]

    #for i in proper:
    #    for i in proper:
    #        subres = copy.copy(proper)
    #        b = subres.remove(i)
    #        a = sum(subres)
    #for i in proper:
    #    sumset = sumset + i
    #    subres.append(sumset)

    #print subres
    #print sumset

    if sumset > number :

        return "weird"
    else:
        return "not weird"

if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 200 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print weird(input[x])