__author__ = 'jeonjiseong'
import struct
import sys

def endians(number):
    endi = sys.byteorder
    if endi == 'little' :
        ltb = struct.pack('>I',number)
        bnum = struct.unpack('I',ltb)
        #print repr(ltb)
        return bnum[0]
    else:
        btl = struct.pack('<I',number)
        lnum = struct.unpack('I',btl)
        return lnum[0]

print endians(4294967295)