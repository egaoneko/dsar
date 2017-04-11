# 열 개씩 끊어 출력하기
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(input):
    res = []
    str = ''
    for i in range(len(input)):
        str += input[i]
        if i % 10 == 9 or len(input) - 1 == i:
            res.append(str)
            str = ''
    return res


class Test(unittest.TestCase):
    def test_action(self):
        actual = action("BaekjoonOnlineJudge")
        expected = ["BaekjoonOn", "lineJudge"]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    input = rl()

    for s in action(input):
        print(s)
    unittest.main()
