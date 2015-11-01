# Xhaeneung Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

for i in xrange(n):
    s = rl().split()
    input.append((s[0], s[1], s[2], s[4]))

dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}


def xhae(l):
    # A operation B
    exp = str(dict[l[0]]) + l[1] + str(dict[l[2]])

    res = eval(exp)

    if res < 0 or res > 10:
        return "No"

    ress = dict[res]
    ress_wc = wc(ress)
    input_wc = wc(l[3])

    if wc_checker(ress_wc, input_wc):
        return "Yes"
    else:
        return "No"


def wc(s):
    wc = {}
    for x in xrange(len(s)):
        if s[x] in wc:
            wc[s[x]] += 1
        else:
            wc[s[x]] = 1
    return wc


def wc_checker(wc1, wc2):
    for w1_key, w1_value in wc1.items():
        if w1_key not in wc2:
            return False
        else:
            if w1_value != wc2[w1_key]:
                return False

    return True


for x in xrange(len(input)):
    print(xhae(input[x]))
