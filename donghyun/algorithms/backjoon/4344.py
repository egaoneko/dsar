# 쳥균은 넘겠지
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(input):
    return input


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action("a"), "a")

if __name__ == '__main__':
    n = int(rl())
    input = []

    for i in range(n):
        s = rl().split()
        input.append(s[1:])

    print(action(input))
    # unittest.main()
