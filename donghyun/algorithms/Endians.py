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
	newByte = [int(byte[3-i], 16) << div[i] for i in range(0,4)]
	
	ret = 0
	for x in newByte:
		ret += x
	return ret

for x in input:
	print(endianConversion(x))
