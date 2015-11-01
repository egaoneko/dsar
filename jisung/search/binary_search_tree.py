__author__ = 'jeonjiseong'

class node:
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return 'Node ['+str(self.data)+']'

class bst:
    def __init__(self,data):
        self.node = node(None,None,data)

    def clear(self):
        self.__init__()

    def searchnode(self,treeset,target):
        if treeset is None:
            return None

        if treeset.data < target:
            return self.searchnode(treeset.left,target)
        elif treeset.data > target:
            return self.searchnode(treeset.right,target)
        else:
            return treeset

    def searchminnode(self,treeset):
        if treeset is None:
            return None

        if treeset.left is None:
            return treeset
        else:
            return self.searchminnode(treeset.left)

    def insertnode(self,treeset,child):
        if treeset.data < child.data:
            if treeset.right == None:
                treeset.right = child
            else:
                treeset.insertnode(treeset.right,child)
        elif treeset.data > child.data:
            if treeset.left == None:
                treeset.left = child
            else:
                treeset.insertnode(treeset.left,child)

    def removenode(self,treeset,parent,target):
        #removed = ""

        if treeset == None:
            return None

        if treeset.data > target:
            removed = self.removenode(treeset.left,treeset,target)
        elif treeset.data < target:
            removed = self.removenode(treeset.right,treeset,target)
        else:           #find the target
            removed = treeset

            if treeset.left is None and treeset.right is None:
                if parent.left is treeset:
                    parent.left = None
                else:
                    parent.right = None
            else:
                if treeset.left is not None and treeset.right is not None:
                    minnode = self.searchminnode(treeset.right)
                    minnode = self.removenode(treeset,None,minnode.data)
                    treeset.data = minnode.data
                else:
                    #temp = ""
                    if treeset.left is not None:
                        temp = treeset.left
                    else:
                        temp = treeset.right

                    if parent.left is treeset:
                        parent.left = temp
                    else:
                        parent.right = temp

        return removed

    def inorderprint(self,treeset):
        if treeset is None:
            return None

        self.inorderprint(treeset.left)
        print self.data
        self.inorderprint(treeset.right)

if __name__ == "__main__":
    n = node(123)
    t = bst(n)
    a = node(22)
    c = node(9911)
    d = node(424)
    t.insertnode(t,a)
    t.insertnode(t,c)
    t.insertnode(t,d)
    t.inorderprint(t)