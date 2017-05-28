# 한수
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(input):
    hansu = 99
    if input < 100:
        return input

    for num in range(100, input+1):
        if is_hansu(num):
            hansu += 1
    return hansu


def is_hansu(num):
    if input < 100:
        return input

    term = None
    while num > 9:
        next_num = int(num/10)
        first = num % 10
        second = next_num % 10
        now_term = second - first

        if term is None:
            term = now_term
        elif term != now_term:
            return False

        num = next_num

    return True


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(110), 99)

if __name__ == '__main__':
    input = int(rl())
    print(action(input))
    unittest.main()
