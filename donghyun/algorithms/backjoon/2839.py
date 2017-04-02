# 설탕배달
# author : Donghyun Seo (egaoneko@naver.com)

import sys

rl = lambda: sys.stdin.readline()

n = int(rl())

if not 3 <= n <= 5000:
    exit()

result = set()
rs3 = int(n/3)
rs5 = int(n/5)

for i3 in range(rs3 + 1):
    s3 = i3 * 3
    if s3 > n:
        break

    for i5 in range(rs5 + 1):
        s5 = i5 * 5
        if s5 > n:
            break
        if s3 + s5 != n:
            continue

        result.add(i3+i5)

result = list(result)
result.sort()

if len(result) > 0:
    print(result[0])
else:
    print(-1)
