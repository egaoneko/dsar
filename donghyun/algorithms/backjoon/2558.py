# A + B - 2
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

s1 = rl()
s2 = rl()

A = int(s1)
B = int(s2)

if not 0<A<10 or not 0<B<10:
    exit()
print(A+B)
