__author__ = 'jeonjiseong'
import sys

r1 = lambda : sys.stdin.readline()
a = int(r1())

def mercy(a):
    if a<1 or a>10:
        print('Not allowed range of numer')
    else:
        while a != 0:
            print 'Hello Algospot!'
            a -= 1

mercy(a)