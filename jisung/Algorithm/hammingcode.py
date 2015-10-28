__author__ = 'jeonjiseong'

import sys

def hammingcode(bystring):
    bystring = bystring.rstrip()

    if len(bystring) > 7:
        "Out of Range"

    strcode = list(bystring)

    intcode = list()

    for i in strcode:
        intcode.append(int(i))

    syndrome = list()

    syndrome.append(intcode[3] ^ intcode[4] ^ intcode[5] ^ intcode[6])
    syndrome.append(intcode[1] ^ intcode[2] ^ intcode[5] ^ intcode[6])
    syndrome.append(intcode[0] ^ intcode[2] ^ intcode[4] ^ intcode[6])

    bystr = ''.join('{0}'.format(d) for d in syndrome)

    if bystr != "000":
        denum = int(bystr,2)

        if denum == 3 or 5 or 6 or 7:
            if intcode[denum-1] == 1:
                intcode[denum-1] = 0
            else:
                intcode[denum-1] = 1

    restr = str(intcode[2]) + str(intcode[4]) + str(intcode[5]) + str(intcode[6])

    return restr

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
        print hammingcode(input[x])