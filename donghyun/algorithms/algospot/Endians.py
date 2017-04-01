# Endians Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
    input.append(int(rl()))


def endianConversion(number):
    div = (24, 16, 8, 0)
    byte = [hex(number >> i & 0xff) for i in div]
    # 2018915346 일때0x12345678의부분 배열을 반환
    # 00010010 00110100 01010110 01111000 (in an Blefuscu computer)

    newByte = [int(byte[3 - i], 16) << div[i] for i in range(0, 4)]
    # Big Endians => Little Endians 로 변환
    # Little Endians의 16진수 부분 값을 10진수 정수로 변환

    ret = 0
    for x in newByte:
        ret += x

    # 부분으로 된 값을 합쳐서 반환함
    return ret


for x in input:
    print(endianConversion(x))
