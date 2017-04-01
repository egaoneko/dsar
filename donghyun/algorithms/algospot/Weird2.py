# Weird Algospot
# author : Donghyun Seo(egaoneko@naver.com)
#
# http://en.wikipedia.org/wiki/Weird_number
# http://oeis.org/A006037
# http://hyulim.tistory.com/254

import sys


# rl = lambda:sys.stdin.readline()
# C = int(rl())
# input = list()

# for i in xrange(C):
#	s = int(rl())
#
#	if s < 2 or s > 500000:
#		print("wrong input")
#		exit()
#	input.append(s)

def divisor(x):
    return [i for i in xrange(1, x) if x % i == 0]


def weird(x):
    l = divisor(x)

    sum = 0
    for i in l:
        sum += i

    # check(l,x)
    if x > sum:
        return "not weird"
    elif not check(l, x):
        return "not weird"

    return "weird"


def check(l, x):
    s = 2 ** len(l)
    ll = len(l)
    print(l)
    for i in xrange(1, s):
        b = i2b(i, ll)
        cl = []
        for j in xrange(ll):
            if int(b[(ll - 1) - j]) == 1:
                cl.append(l[j])
        sum = 0
        for j in cl:
            sum += j

        # print(i,b,sum)
        if sum == x:
            return False
        elif sum > x:
            return True

    return False


def i2b(i, l):
    s = ''
    while i > 0:
        s = str(i & 1) + s
        i = i >> 1
    return s.zfill(l)


# for i in xrange(C):
#	#weird(input[i])
#	print(weird(input[i]))

for i in xrange(1, 500001):
    print(str(i) + ": " + weird(i))
