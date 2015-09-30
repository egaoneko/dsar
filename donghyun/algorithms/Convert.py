# Convert Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda:sys.stdin.readline()

n = int(rl())
input = list()

for i in range(n):
	s = rl().split()
	input.append((float(s[0]), s[1]))

c = {
	"kg"	: (2.2046, "lb"),
	"lb"	: (0.4536, "kg"),
	"l"		: (0.2642, "g"),
	"g"		: (3.7854, "l")
}

for i, x in enumerate(input):
	print("%d %.4f %s" % (i+1, c[x[1]][0]*x[0], c[x[1]][1]))
