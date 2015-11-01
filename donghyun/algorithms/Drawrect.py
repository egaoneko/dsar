# Drawrect Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
    l = list()
    for j in range(3):
        xy = rl().split()
        l.append((int(xy[0]), int(xy[1])))

    input.append(l)


def drawRect(l):
    x1 = l[0][0]
    y1 = l[0][1]

    x2 = l[1][0]
    y2 = l[1][1]

    x3 = l[2][0]
    y3 = l[2][1]

    xy12 = rectLength(x1, y1, x2, y2)
    xy13 = rectLength(x1, y1, x3, y3)
    xy23 = rectLength(x2, y2, x3, y3)

    if xy12 > xy13 and xy12 > xy23:
        x = x1 + x2 - x3
        y = y1 + y2 - y3
    if xy13 > xy12 and xy13 > xy23:
        x = x1 + x3 - x2
        y = y1 + y3 - y2
    if xy23 > xy12 and xy23 > xy13:
        x = x2 + x3 - x1
        y = y2 + y3 - y1

    return x, y


def rectLength(x1, y1, x2, y2):
    return pow(pow(abs(x2 - x1), 2) + pow(abs(y2 - y1), 2), 0.5)


for i in input:
    x, y = drawRect(i)
    print("%d %d" % (x, y))
