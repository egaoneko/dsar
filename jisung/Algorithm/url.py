__author__ = 'jeonjiseong'

import sys

def url(stringarray):
    changestring = stringarray.rstrip()

    if len(changestring) > 80:
        return "Error : Out of range"

    l = [("%20", " "), ("%21", "!"), ("%24", "$"), ("%28", "("), ("%29", ")"), ("%2a", "*"), ("%25", "%")]

    for i in xrange(len(l)):
        changestring = changestring.replace(l[i][0],l[i][1])

    return changestring

'''
    changelist = list(changestring)
    for i in changelist:
        if i == "%":
            ind = changelist.index(i)
            tempstring = changelist[ind+1] + changelist[ind+2]
            for k in dict.iterkeys():
                if k == tempstring:
                    #print changelist
                    changelist.pop(ind+1)
                    #print changelist
                    changelist.pop(ind+1)
                    #print changelist
                    changelist[ind] = dict.get(tempstring)
                    #print changelist
                    break
                # else:
                #  for c in dict.iterkeys():
                #     if c == i:
                #         changelist[ind] = dict.get(c)
        else:
            for k in dict.iterkeys():
                if k == i:
                    ind = changelist.index(i)
                    changelist[ind] = dict.get(k)


    changestring = "".join(changelist)
    return changestring
'''
if __name__ == "__main__":

    r1 = lambda : sys.stdin.readline()
    n = int(r1())

    if n > 100 or n < 1:
        print "Wrong Input"
        exit()

    input = list()

    for i in range(n):
        input.append(str(r1()))

    for x in xrange(input.__len__()):
        print url(input[x])