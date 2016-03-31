import jisung.list.Linkedlist_norm as madnList
__author__ = 'jeonjiseong'

def sequentialsearch(alist, target):
    match = ''

    for i in alist:
        if i == target:
            match = i
            break

    if match is '':
        match = "no data"

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
    alist = [1,2,3,4,5,6,7,8]
    a=sequentialsearch(alist,9)
    print(a)