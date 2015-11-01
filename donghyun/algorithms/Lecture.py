# Lecture Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
    input.append(rl().rstrip())


def Lecture(str):
    l = len(str)
    sl = list()

    for i in range(0, l, 2):
        sl.append(str[i:i + 2])

    sl.sort()

    ret = ''
    for x in sl:
        ret += x
    return ret


for x in input:
    print(Lecture(x))
