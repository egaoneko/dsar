# Encrypt Algospot
# author : Donghyun Seo(egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
input = list()

for i in range(n):
    input.append(rl().rstrip())

for s in input:
    sO = ''.join([x[1] for x in list(filter(lambda x: x[0] % 2 == 0, enumerate(list(s))))])
    sE = ''.join([x[1] for x in list(filter(lambda x: x[0] % 2 != 0, enumerate(list(s))))])

    print sO + sE
