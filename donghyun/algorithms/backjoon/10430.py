# 나머지
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

s = rl().split()

A = int(s[0])
B = int(s[1])
C = int(s[2])

if not 1<A<10001 or not 1<B<10001 or not 1<C<10001:
    exit()

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
