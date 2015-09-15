__author__ = 'jeonjiseong'

#node = dict(0:"value")

class node:
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return 'Node ['+str(self.data)+']'

class LinkedList:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def __str__(self):
        if self.firstNode != None:
            current = self.firstNode
            out = 'LinkedList \n[' +str(current.data) +']\n'
            while current.nextNode != None:
                current = current.nextNode
                out += '[' + str(current.data) +']'+ '\n'
            return out
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def addNode(self,value):
        if self.firstNode is None:
            self.firstNode = node(value,None)
            self.lastNode = self.firstNode
        elif self.lastNode == self.firstNode:
            self.lastNode = node(value,None)
            self.firstNode.nextNode = self.lastNode
        else:
            current = node(value,None)
            self.lastNode.nextNode = current
            self.lastNode = current

    def getNode(self,location): # Index of this data starts with 0
        head = self.firstNode
        i = 0
        target = head
        find = head
        while i != location :
            target = find.nextNode
            find = target
            i+=1
        return target

    def insertNode(self,location,value): #think about tail node
        curNode = self.getNode(location)
        print curNode
        if curNode.nextNode is None:
            self.addNode(value)
        else:
            nextLink = curNode.nextNode
            newNode = node(value,nextLink)
            curNode.nextNode = newNode

    def deleteNode(self,location): #think about deleting head node & tail node
        curNode = self.getNode(location)
        if curNode == self.firstNode :
            self.firstNode = curNode.nextNode
        elif curNode == self.lastNode:
            preNode = self.getNode(location-1)
            preNode.nextNode = None
            self.lastNode = preNode
        else:
            preNode = self.getNode(location-1)
            preNode.nextNode = curNode.nextNode

    def countNode(self):
        curNode = self.firstNode
        count = 0

        while curNode is not None:
            curNode = curNode.nextNode
            count += 1

        return count

'''
l = LinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
print l
print l.getNode(2)
l.insertNode(2,5)
print l
l.deleteNode(2)
print l
l.deleteNode(3)
print l
print l.countNode()
l.insertNode(0,0)
print l
l.insertNode(1,10)
print l
'''