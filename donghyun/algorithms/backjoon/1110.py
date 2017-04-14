# 더하기 사이클
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(input):
    return add_cycle(input, 1, input)


def add_cycle(origin, cycle, current_num):
    if current_num < 10:
        first = 0
    else:
        first = int(current_num / 10)

    second = current_num % 10
    third = first + second

    new_num = second * 10 + third % 10

    if cycle > 0 and origin == new_num:
        return cycle
    else:
        cycle += 1
        return add_cycle(origin, cycle, new_num)


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(26), 4)

if __name__ == '__main__':
    input = int(rl())
    print(action(input))
    unittest.main()
