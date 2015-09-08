__author__ = 'jeonjiseong'
import struct
import sys

r1 = lambda : sys.stdin.readline()
n = int(r1())
input = list()

for i in range(n):
    input.append(int(r1()))

def endians(number):
    endi = sys.byteorder # 입력 값이 빅 엔디안인지 리틀엔디안 인지 판별 -> return 값은 little 또는 big의 스트링값
    if endi == 'little' :
        ltb = struct.pack('>I',number) # struct.pack의 매개변수 >는 빅엔디안으로의 변환을 의미 I는 unsigned int형을 의미 >는 리틀엔디안으로의 변환을 의
        bnum = struct.unpack('I',ltb) # pack은 값을 매개변수의 format에 따라 변경, unpack은 그 반대를 실행
        #print repr(ltb)
        return bnum[0]
    else:
        btl = struct.pack('<I',number)
        lnum = struct.unpack('I',btl)
        return lnum[0]

for x in input:
    print endians(x)