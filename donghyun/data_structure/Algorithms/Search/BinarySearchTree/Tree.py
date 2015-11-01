# -*- coding: utf-8 -*-

__author__ = 'Donghyun(egaoneko@naver.com)'
__version__ = '1.0'


class Tree:
    '''Tree Classa.

    This tree class is used for storing datas.
    And this class is consist of tree.'''

    def __init__(self, data=None, leftChild=None, rightChild=None):
        self.__data__ = data
        self.__leftChild__ = leftChild
        self.__rightChild__ = rightChild

    def getData(self):
        return self.__data__

    def setData(self, data):
        self.__data__ = data

    def getLeftSubTree(self):
        return self.__leftChild__

    def getRightSubTree(self):
        return self.__rightChild__

    def setLeftSubTree(self, leftChild):
        self.__leftChild__ = leftChild

    def setRightSubTree(self, rightChild):
        self.__rightChild__ = rightChild

    @classmethod
    def preorderTraverse(cls, tree, action):
        if tree == None: return

        action(tree.__data__)
        cls.preorderTraverse(tree.__leftChild__, action)
        cls.preorderTraverse(tree.__rightChild__, action)

    @classmethod
    def inorderTraverse(cls, tree, action):
        if tree == None: return

        cls.inorderTraverse(tree.__leftChild__, action)
        action(tree.__data__)
        cls.inorderTraverse(tree.__rightChild__, action)

    @classmethod
    def postorderTraverse(cls, tree, action):
        if tree == None: return

        cls.postorderTraverse(tree.__leftChild__, action)
        cls.postorderTraverse(tree.__rightChild__, action)
        action(tree.__data__)

    def removeLeftSubTree(self):
        delNode = self.__leftChild__
        self.__leftChild__ = None
        return delNode

    def removeRightSubTree(self):
        delNode = self.__rightChild__
        self.__rightChild__ = None
        return delNode

    def changeLeftSubTree(self, sub):
        self.__leftChild__ = sub

    def changeRightSubTree(self, sub):
        self.__rightChild__ = sub


if __name__ == '__main__':
    tree = Tree(1)
    leftChild = Tree(2)
    rightChild = Tree(3)
    tree.setLeftSubTree(leftChild)
    tree.setRightSubTree(rightChild)

    tree2 = Tree(4, Tree(5), Tree(6))
    tree.getLeftSubTree().setRightSubTree(tree2)


    def printData(x):
        print(x)


    Tree.inorderTraverse(tree, lambda x: printData(x))
