# 구구단
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(n, i, n*i))
