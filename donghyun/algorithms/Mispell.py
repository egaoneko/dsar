# Mispell Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda:sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
	str = rl().split()
	input.append((int(str[0]), str[1]))

def mispell(input):
	return [str[:mis-1] + str[mis:] for mis, str in input]

for idx, str in enumerate(mispell(input)):
	print("%d %s" % (idx+1, str))
