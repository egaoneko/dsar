# 별찍기 - 4
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())

for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * i)
