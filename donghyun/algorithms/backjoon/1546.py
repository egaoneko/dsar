# 평균
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(L):
    max = 0
    for l in L:
        if max < l:
            max = l

    sum = 0
    for l in L:
        sum += l / max * 100
    return sum / len(L)


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action([40, 80, 60]), 75)

if __name__ == '__main__':
    input = rl()
    N = int(input)

    input = rl().split()
    L = []
    for n in range(N):
        L.append(int(input[n]))
    print("%.2f" % action(L))
    unittest.main()
