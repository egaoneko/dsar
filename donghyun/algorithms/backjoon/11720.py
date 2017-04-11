# 숫자의 합
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(n, input):
    sum = 0
    for i in range(n):
        sum += int(input[i])
    return sum


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(5, "54321"), 15)

if __name__ == '__main__':
    n = int(rl())
    input = rl()
    print(action(n, input))
    unittest.main()
