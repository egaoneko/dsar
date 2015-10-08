__author__ = 'jeonjiseong'

class binarytree:
    def __init__(self,data=None,leftnode=None,rightnode=None):
        self.data = data
        self.leftnode = leftnode
        self.rightnode = rightnode

    def clear(self):
        self.__init__()

    def getdata(self):
        return self.data

    def addleftnode(self,leftnode):
        self.leftnode = leftnode

    def addrightnode(self,rightnode):
        self.rightnode = rightnode

    def preorder(self,node):
        if node is None:
            return

        print node.getdata()
        self.preorder(node.leftnode)
        self.preorder(node.rightnode)

    def inorder(self,node):
        if node is None:
            return

        self.inorder(node.leftnode)
        print node.getdata()
        self.inorder(node.rightnode)

    def postorder(self,node):
        if node is None:
            return

        self.postorder(node.leftnode)
        self.postorder(node.rightnode)
        print node.getdata()

if __name__ == "__main__":
    t = binarytree('A')
    leftchild = binarytree('B')
    rightchild = binarytree('E')
    t.addleftnode(leftchild)
    t.addrightnode(rightchild)
    leftchild.addleftnode(binarytree('C'))
    leftchild.addrightnode(binarytree('D'))
    rightchild.addleftnode(binarytree('F'))
    rightchild.addrightnode(binarytree('G'))

    t.preorder(t)
    t.postorder(t)
    t.inorder(t)