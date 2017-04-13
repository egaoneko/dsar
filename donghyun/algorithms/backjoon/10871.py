# X보다 작은 수
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(X, L):
    minL = []
    for l in L:
        if l < X:
            minL.append(l)
    return minL


class Test(unittest.TestCase):
    def test_action(self):
        X = 5
        L = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
        expected = [1, 4, 2, 3]
        actual = action(X, L)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    input = rl().split()
    N = int(input[0])
    X = int(input[1])

    input = rl().split()
    L = []
    for n in range(N):
        L.append(int(input[n]))

    res = action(X, L)
    for r in res:
        print(r)
    unittest.main()
