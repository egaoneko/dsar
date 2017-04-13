#
# author : Donghyun Seo (egaoneko@naver.com)

import sys
import unittest


def rl():
    return sys.stdin.readline()


def fl(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return remove_new_line(lines)


def remove_new_line(lines):
    return [line.replace('\n', '') for line in lines]


def action(input):
    return input


class Test(unittest.TestCase):
    def setUp(self):
        self.file_input = fl("input.txt")
        self.file_result = fl("result.txt")

    def test_action(self):
        line_length = len(self.file_input)
        for index in range(line_length):
            self.assertEqual(
                action(self.file_input[index]), self.file_result[index])


if __name__ == '__main__':
    input = rl()
    print(action(input))
    unittest.main()
