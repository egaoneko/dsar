# 시험 성적
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(input):

    if 90 <= input <= 100:
        return "A"
    elif 80 <= input <= 89:
        return "B"
    elif 70 <= input <= 79:
        return "C"
    elif 60 <= input <= 69:
        return "D"
    else:
        return "F"


class Test(unittest.TestCase):
    def test_action(self):
        self.assertEqual(action(90), "A")
        self.assertEqual(action(80), "B")
        self.assertEqual(action(70), "C")
        self.assertEqual(action(60), "D")
        self.assertEqual(action(50), "F")

if __name__ == '__main__':
    input = int(rl())
    print(action(input))
    unittest.main()
