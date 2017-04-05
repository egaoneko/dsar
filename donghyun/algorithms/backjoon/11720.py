# 숫자의 합
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(n):
    sum = 0
    while n/10 > 0:
        sum += n % 10
        n = int(n/10)
    return sum


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(54321), 15)

if __name__ == '__main__':
    rl()
    input = int(rl())
    print(action(input))
    unittest.main()
