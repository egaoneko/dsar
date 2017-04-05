# 합
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(3), 6)

if __name__ == '__main__':
    input = int(rl())
    print(action(input))
    unittest.main()
