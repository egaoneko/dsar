# 2007년
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def rl():
    return sys.stdin.readline()


def action(month, day):
    total_day = 0
    for (i, m) in enumerate(range(month)):
        total_day += MONTH[i]
    total_day += day
    week = total_day % 7
    return WEEK[week]


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(1, 1), WEEK[1])
        self.assertEqual(action(7, 7), WEEK[6])

if __name__ == '__main__':
    input = rl().split()
    month, day = int(input[0]), int(input[1])
    print(action(month, day))
    unittest.main()
