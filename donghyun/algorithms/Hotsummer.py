# Hotsummer Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

T = int(rl())
input = list()

for i in range(T):
    g = int(rl())
    w = rl()
    input.append((g, w))


def hotsummer(input):
    wl = input[1].split()

    s = 0
    for w in wl:
        s += int(w)

    if input[0] >= s:
        return "YES"
    else:
        return "NO"


for x in input:
    print(hotsummer(x))
