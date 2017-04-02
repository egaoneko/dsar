# 그대로 출력하기 2
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import re

def action(input):
    print(input, end="")

rl = lambda: sys.stdin.readline()

line = 0
while True:
    s = rl()
    line += 1

    if line > 100:
        exit()

    if not bool(re.match('[a-zA-Z0-9 \n]+', s)):
        exit()

    action(s)
