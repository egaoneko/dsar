# Hammingcode Algospot
# author : Donghyun Seo(egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()
T = int(rl())
input = list()

for i in xrange(T):
    input.append(rl().rstrip())


def hammingcode(s):
    c1 = int(s[0]) ^ int(s[2]) ^ int(s[4]) ^ int(s[6])
    c2 = (int(s[1]) ^ int(s[2]) ^ int(s[5]) ^ int(s[6])) << 1
    c3 = (int(s[3]) ^ int(s[4]) ^ int(s[5]) ^ int(s[6])) << 2

    c = c3 + c2 + c1 - 1

    if c != -1:
        s = s[0:c] + str(int(s[c]) ^ 1) + s[c + 1:]
    return s[2] + s[4] + s[5] + s[6]


for i in xrange(T):
    print(hammingcode(input[i]))
