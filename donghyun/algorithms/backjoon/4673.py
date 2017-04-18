# 셀프넘버
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action(n):
    self_dict = {k: True for k in range(1, n+1)}

    for i in range(1, n+1):
        sn = d(i)
        if sn > n:
            continue
        self_dict[sn] = False

    self_list = [k for k, v in self_dict.items() if v]

    return self_list


def d(num):
    sum = num
    while num > 0:
        sum += num % 10
        num = int(num/10)
    return sum


class Test(unittest.TestCase):
    def test_action(self):
        expected = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
        self.assertEqual(action(100), expected)

    def test_self_number_75(self):
        self.assertEqual(d(75), 87)

    def test_self_number_33(self):
        self.assertEqual(d(33), 39)

    def test_self_number_2(self):
        self.assertEqual(d(2), 4)

    def test_self_number_1(self):
        self.assertEqual(d(1), 2)

if __name__ == '__main__':
    self_numbers = action(10000)
    for number in self_numbers:
        print(number)
    unittest.main()
