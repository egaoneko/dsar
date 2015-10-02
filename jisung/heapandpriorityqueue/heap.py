__author__ = 'jeonjiseong'

from array import *

class heap:
    def __init__(self):
        self.usedsize = 0
        self.nodes = array('i',[])

    def clear(self):
        self.__init__()

    def printnodes(self):
        print "Heap",
        for i in self.nodes:
            print "%d " % i,
        print ""

    def getparent(self,index):
        return (index - 1)/2

    def getleftchild(self,index):
        return (2 * index)+1

    def swapnode(self,index1,index2):
        tempnode = self.nodes[index1]
        self.nodes[index1] = self.nodes[index2]
        self.nodes[index2] = tempnode

    def insertheap(self,newdata):
        curposition = self.usedsize
        parposition = self.getparent(curposition)

        self.nodes.insert(curposition,newdata)

        while curposition > 0 and self.nodes[curposition] < self.nodes[parposition]:
            self.swapnode(curposition,parposition)

            curposition = parposition
            parposition = self.getparent(curposition)

        self.usedsize += 1

    def deletemin(self):
        parentposition = 0

        root = self.nodes[0]
        self.nodes[0] = 0
        self.usedsize -= 1
        self.swapnode(0,self.usedsize)

        leftposition = self.getleftchild(0)
        rightposition = leftposition + 1

        while 1 :
            selectedchild = 0

            if leftposition >= self.usedsize:
                break

            if rightposition >= self.usedsize:
                selectedchild = leftposition
            else:
                if self.nodes[leftposition] > self.nodes[rightposition]:
                    selectedchild = rightposition
                else:
                    selectedchild = leftposition

            if self.nodes[selectedchild] < self.nodes[parentposition]:
                self.swapnode(parentposition,selectedchild)
                parentposition = selectedchild
            else:
                break

            leftposition = self.getleftchild(parentposition)
            rightposition = leftposition + 1

        self.nodes.remove(0)


if __name__ == "__main__":
    h = heap()
    h.insertheap(12)
    h.insertheap(87)
    h.insertheap(111)
    h.insertheap(34)
    h.insertheap(16)
    h.insertheap(75)
    h.printnodes()
    h.deletemin()
    h.printnodes()
    h.deletemin()
    h.printnodes()
    h.deletemin()
    h.printnodes()