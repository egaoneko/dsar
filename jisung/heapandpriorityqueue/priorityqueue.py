__author__ = 'jeonjiseong'

from array import *

class priorityqueue:
    def __init__(self):
        self.usedsize = 0
        self.priority = array('i',[])
        self.data = list()

    def clear(self):
        self.data.__init__()
        self.priority.__init__()
        self.__init__()

    def printnodes(self):
        print "Priority queue"
        print "Data"
        for i in self.data:
            print "%s " % i,

        print ""
        print "Priority"
        for i in self.priority:
            print "%d" %i,

        print ""

    def getparent(self,index):
        return (index - 1)/2

    def getleftchild(self,index):
        return (2 * index)+1

    def swapnode(self,index1,index2):
        tempnode = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = tempnode

        tempnode = self.priority[index1]
        self.priority[index1] = self.priority[index2]
        self.priority[index2] = tempnode

    def isempty(self):
        return self.usedsize == 0

    def enqueue(self,newpriority,newdata):
        currentposition = self.usedsize
        parentposition = self.getparent(currentposition)

        self.data.insert(currentposition,newdata)
        self.priority.insert(currentposition,newpriority)

        while currentposition > 0 and self.priority[currentposition] < self.priority[parentposition]:
            self.swapnode(currentposition,parentposition)

            currentposition = parentposition
            parentposition = self.getparent(currentposition)

        self.usedsize += 1

    def dequeue(self):
        parentposition = 0

        rootdata = self.data[0]
        self.data[0] = 0
        rootpriority = self.priority[0]
        self.priority[0] = 0
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
                if self.priority[leftposition] > self.priority[rightposition]:
                    selectedchild = rightposition
                else:
                    selectedchild = leftposition

            if self.priority[selectedchild] < self.priority[parentposition]:
                self.swapnode(parentposition,selectedchild)
                parentposition = selectedchild
            else:
                break

            leftposition = self.getleftchild(parentposition)
            rightposition = leftposition + 1

        self.data.remove(0)
        self.priority.remove(0)

        return [rootdata,rootpriority]

if __name__ == "__main__":
    p = priorityqueue()
    p.enqueue(34,"coding")
    p.enqueue(12,"meeting")
    p.enqueue(87,"typing")
    p.enqueue(45,"coffee")
    p.enqueue(35,"debugging")
    p.enqueue(66,"brushing")

    p.printnodes()

    print p.dequeue()

    p.printnodes()

    print p.dequeue()
    print p.dequeue()
    print p.dequeue()
    print p.dequeue()


