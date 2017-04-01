# 
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
    s = rl().split()
    input.append((s[0], s[1]))
