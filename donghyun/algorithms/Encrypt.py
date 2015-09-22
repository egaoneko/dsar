# Encrypt Algospot
# author : Donghyun Seo(egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
input = list()

for i in range(n):
	input.append(rl().rstrip())

def encryptMessage(str):
	l = len(str)
	n = 0
	if l%2!=0:
		n = (l>>1)+1
	else:
		n = l>>1

	sO = ''
	sE = ''

	for i in range(0, n):
		sO += str[2*i]

		if l%2 != 0 and i == n-1:
			break;

		sE += str[2*i+1]

	return sO + sE

for x in input:
	print(encryptMessage(x))
		
