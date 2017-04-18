#
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def action():
    return "a"


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_action(self):
        self.assertEqual(action(), "a")

if __name__ == '__main__':
    print(action())
    unittest.main()
