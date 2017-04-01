# Convert Algospot
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())
input = list()

day_dic = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}
last_day = (31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);

for i in range(n):
    s = rl().split()
    input.append((int(s[0]), int(s[1]), s[2]))

for x in input:

    index = day_dic[x[2]]
    week = [0, 0, 0, 0, 0, 0, 0]

    i = index
    while i >= 0:
        day = x[1] - (index - i)

        if day > 0:
            week[i] = day
        else:
            week[i] = last_day[x[0]-1] + day

        i -= 1

    i = index
    while i < 7:
        day = x[1] + (i - index)

        if day <= last_day[x[0]]:
            week[i] = day
        else:
            week[i] = day - last_day[x[0]]

        i += 1

    for d in week:
        print d,
    print
