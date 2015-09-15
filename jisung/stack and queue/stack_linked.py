__author__ = 'jeonjiseong'

import jisung.list.linkedlist_norm as madnList

class Stack:
    def __init__(self,list=None,top=None):
        self.list = list
        self.top = top

    def __str__(self):
        if self.list.firstNode != None:
            curList = self.list
            out = 'Stack \n[' +str(curList.firstNode.data) +']\n'
            curNode = curList.firstNode
            while curNode.nextNode is not None:
                current = curNode.nextNode
                out += '[' + str(current.data) +']'+ '\n'
                curNode = current
            return out
        return 'Stack []'

    def createList(self,data):
        l = madnList.LinkedList()
        l.addNode(data)
        self.list = l
        self.top = l.firstNode

    def clear(self):
        self.list.clear()
        self.__init__()

    def push(self,data):
        if self.list is None:
            self.createList(data)
        else:
            curList = self.list
            curList.addNode(data)
            self.list = curList
            self.top = curList.lastNode

    def pop(self):
        topNode = self.top

        if self.list.firstNode is topNode :
            self.clear()
        else:
            curList = self.list
            listCount = curList.countNode()
            curList.deleteNode(listCount-1)
            self.list = curList
            self.top = curList.lastNode

    def getSize(self):
        return self.list.countNode()

    def isEmpty(self):
        if self.list.countNode() is 0:
            return 'true'
        else:
            return 'false'

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print s
print s.getSize()
print s.isEmpty()
s.pop()
s.pop()
print s
print s.getSize()
s.pop()
s.pop()
print s
print s.isEmpty()

