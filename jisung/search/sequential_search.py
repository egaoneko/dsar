__author__ = 'jeonjiseong'

import jisung.list.Linkedlist_norm as madnList

def sequentialsearch(head,target):
    current = head
    match = ''

    while current is not None:
        if current.data == target:
            match = current
            break
        else:
            current = current.nextNode

    return match

def movetofront(head,target):
    current = head
    previous = ""
    match = ""

    while current is not None:
        if current.data == target:
            match = current
            if previous is not None:
                previous.nextNode = current.nextNode
                current.nextNode = head
                head = current
                break
            else:
                previous = current
                current = current.nextNode
        return match

def transpose(head,target):
    current = head
    pprevious = ""
    previous = ""
    match = ""

    while current is not None:
        if current.data is target:
            match = current
            if previous is not None:
                if pprevious is not None:
                    pprevious.nextNode = current
                else:
                    head = current

                previous.nextNode = current.nextNode
                current.nextNode = previous
            break
        else:
            if previous is not None:
                pprevious = previous
                previous = current
                current = current.nextNode

    return match

if __name__ == "__main__":
    l = madnList.LinkedList()
    l.addNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    l.insertNode(2,5)
    l.deleteNode(2)
    l.deleteNode(3)
    l.insertNode(0,0)
    l.insertNode(1,10)
    print l
    findnode = sequentialsearch(l.getNode(0),2)
    print findnode