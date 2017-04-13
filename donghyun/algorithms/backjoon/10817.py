# 세 수
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(i0, i1, i2):

    if i0 > i1:
        i0, i1 = i1, i0
    if i1 > i2:
        i1, i2 = i2, i1
    if i0 > i1:
        i0, i1 = i1, i0

    return i1


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(20, 30, 10), 20)
        self.assertEqual(action(30, 30, 10), 30)
        self.assertEqual(action(40, 40, 40), 40)
        self.assertEqual(action(20, 10, 10), 10)

if __name__ == '__main__':
    input = rl().split()
    print(action(int(input[0]), int(input[1]), int(input[2])))
    unittest.main()
