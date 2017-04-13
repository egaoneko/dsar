# 쳥균은 넘겠지
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


def action(line):
    line = line.split()
    size = int(line[0])
    scores = [int(score) for score in line[1:]]
    avg = get_avg(scores, size)
    over_cnt = get_over_avg_cnt(avg, scores)
    return "%.3f%%" % (over_cnt/size*100)


def get_avg(scores, size):
    sum = 0
    for score in scores:
        sum += score

    return sum / size


def get_over_avg_cnt(avg, scores):
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    return cnt


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
    n = int(rl())
    for i in range(n):
        print(action(rl()))
    unittest.main()
