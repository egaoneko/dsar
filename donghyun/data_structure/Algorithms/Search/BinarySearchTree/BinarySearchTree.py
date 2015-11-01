# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


import Tree

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        pNode = None  # Parent Node
        cNode = self.root  # Current Node
        nNode = None  # New Node

        while cNode is not None:
            if data == cNode.getData():
                return

            pNode = cNode

            if cNode.getData() > data:
                cNode = cNode.getLeftSubTree()
            else:
                cNode = cNode.getRightSubTree()

        nNode = Tree.Tree(data)

        if pNode is not None:
            if data < pNode.getData():
                pNode.setLeftSubTree(nNode)
            else:
                pNode.setRightSubTree(nNode)
        else:
            self.root = nNode

    def search(self, target):
        cNode = self.root
        cd = None  # Current Data

        while cNode is not None:
            cd = cNode.getData()

            if target == cd:
                return cNode
            elif target < cd:
                cNode = cNode.getLeftSubTree()
            else:
                cNode = cNode.getRightSubTree()

        return None

    def getNodeData(self, node):
        return node.getData()

    def remove(self, target):
        pVRoot = Tree.Tree()
        pNode = pVRoot
        cNode = self.root
        dNode = None

        pVRoot.changeRightSubTree(self.root)

        while cNode is not None and cNode.getData() != target:
            pNode = cNode

            if target < cNode.getData():
                cNode = cNode.getLeftSubTree()
            else:
                cNode = cNode.getRightSubTree()

        if cNode is None:
            return None

        dNode = cNode

        if dNode.getLeftSubTree() is None and dNode.getRightSubTree() is None:
            if pNode.getLeftSubTree() == dNode:
                pNode.removeLeftSubTree()
            else:
                pNode.removeRightSubTree()
        elif dNode.getLeftSubTree() is None or dNode.getRightSubTree() is None:
            dcNode = None

            if dNode.getLeftSubTree() is not None:
                dcNode = dNode.getLeftSubTree()
            else:
                dcNode = dNode.getRightSubTree()

            if pNode.getLeftSubTree() == dNode:
                pNode.changeLeftSubTree(dcNode)
            else:
                pNode.changeRightSubTree(dcNode)
        else:
            mNode = dNode.getRightSubTree()
            mpNode = dNode

            while mNode.getLeftSubTree() is not None:
                mpNode = mNode
                mNode = mNode.getLeftSubTree()

            delData = dNode.getData()
            dNode.setData(mNode.getData())

            if mpNode.getLeftSubTree() == mNode:
                mpNode.changeLeftSubTree(mNode.getRightSubTree())
            else:
                mpNode.changeRightSubTree(mNode.getRightSubTree())

            dNode = mNode
            dNode.setData(delData)

        if pVRoot.getRightSubTree() != self.root:
            self.root = pVRoot.getRightSubTree()

        return dNode

    def showAll(self):
        def printData(x):
            print x,

        Tree.Tree.inorderTraverse(bst.root, lambda x: printData(x))


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(9)
    bst.insert(1)
    bst.insert(6)
    bst.insert(2)
    bst.insert(8)
    bst.insert(3)
    bst.insert(5)

    sNode = bst.search(1)
    if sNode is None:
        print("Search Fail")
    else:
        print("Search Success: %d" % (sNode.getData()))

    sNode = bst.search(4)
    if sNode is None:
        print("Search Fail")
    else:
        print("Search Success: %d" % (sNode.getData()))

    sNode = bst.search(6)
    if sNode is None:
        print("Search Fail")
    else:
        print("Search Success: %d" % (sNode.getData()))

    sNode = bst.search(7)
    if sNode is None:
        print("Search Fail")
    else:
        print("Search Success: %d" % (sNode.getData()))

    bst.showAll()
    print
    bst.remove(8)
    bst.remove(5)
    bst.showAll()
    print
    bst.remove(3)
    bst.showAll()
