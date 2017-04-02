# 별찍기 - 2
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())

for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)
