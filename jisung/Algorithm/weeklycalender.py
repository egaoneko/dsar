__author__ = 'jeonjiseong'

import sys

def calender(stringset):
    valist = stringset.split()
    valist[0] = int(valist[0])
    valist[1] = int(valist[1])
    valist[2] = valist[2].lower().rstrip()

    day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    if valist[0] < 1 or valist[0] > 12:
        return "Wrong month"
    elif valist[1] < 1 or valist[1] > 31:
        return "Wrong date"
    elif valist[2] not in day:
        return "Wrong day"

    indexday = day.index(valist[2])

    sunday = valist[1] - indexday

    beformon = 0

    if sunday < 1:
        for i in xrange(7):
            if sunday + i == 0:
                beformon = i
                break

    exactmon = valist[0]

    if beformon != 0 or sunday == 0:
        if valist[0] == 1:
            exactmon = 12
            beforday = month.get(exactmon)
        else:
            exactmon = valist[0] - 1
            beforday = month.get(exactmon)
        sunday = beforday - beformon

    dayslist = list()
    for i in xrange(7):
        if sunday > month.get(exactmon):
            sunday = 1
        dayslist.append(sunday)
        sunday = sunday+1

    daystring = ' '.join(str(e) for e in dayslist)
    return daystring


if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print calender(input[x])