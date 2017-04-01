# Uri Algospot
# author : Donghyun Seo(egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
input = list()

for i in xrange(n):
    input.append(rl().replace("\n", ""))

l = [("%20", " "), ("%21", "!"), ("%24", "$"), ("%28", "("), ("%29", ")"), ("%2a", "*"), ("%25", "%")]


# % position problem %252a

def uri(str):
    for i in xrange(len(l)):
        str = str.replace(l[i][0], l[i][1])

    return str


for x in xrange(len(input)):
    print(uri(input[x]))
