__author__ = 'jeonjiseong'

import jisung.list.linkedlist_norm as madnList

class Queue:
    def __init__(self,front=None,rear=None):
        self.front = front
        self.rear = rear
        self.count = 0

    def __str__(self):
        if self.front is not None:
            currNode = self.front
            out = 'Queue \n[' +str(currNode.data) +']\n'
            while currNode.nextNode is not None:
                current = currNode.nextNode
                out += '[' + str(current.data) +']'+ '\n'
                currNode = current
            return out
        return 'Queue []'

    def createQueue(self,data):
        s = madnList.LinkedList()
        s.addNode(data)
        self.front = s.firstNode
        self.rear = s.firstNode
        self.count += 1

    def clear(self):
        self.__init__()

    def enQueue(self,data):
        if self.front is None:
            self.createQueue(data)
        else:
            newNode = madnList.node(data,None)
            self.rear.nextNode = newNode #change value of front.nextNode to newNode
            self.rear = newNode
            self.count += 1

    def deQueue(self):
        if self.front.nextNode is None:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.nextNode
        self.count -= 1

    def isEmpty(self):
        if self.count is 0:
            return 'true'
        else:
            return 'false'


q = Queue()
print q
print q.count
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
print q
print q.count
q.deQueue()
q.deQueue()
print q
print q.count
print q.isEmpty()