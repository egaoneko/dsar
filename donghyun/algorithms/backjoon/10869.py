# 사칙연산
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

s = rl().split()

A = int(s[0])
B = int(s[1])

if not 0<A<10001 or not 0<B<10001:
    exit()

print(A + B)
print(A - B)
print(A * B)
print(int(A/B))
print(A % B)
