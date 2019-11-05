# Node and Reference Binary Tree Implementation

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild
    

    def getRightChild(self):
        return self.rightChild

    
    def setRootVal(self, rootObj):
        self.key = rootObj
    
    def getRootVal(self):
        return self.key

def buildTree():
    t = BinaryTree('a')
    
    t.insertLeft('b')
    t.getLeftChild().insertRight('d')

    t.insertRight('c')
    t.getRightChild().insertLeft('e')
    t.getRightChild().insertRight('f')

    return t

if __name__ == "__main__":
    ttree = buildTree()
    print(ttree)
    print(ttree.getRightChild().getRootVal())
    print(ttree.getLeftChild().getRightChild().getRootVal())
    print(ttree.getRightChild().getLeftChild().getRootVal())


    print(ttree.getRightChild().getRootVal() =='c')
    print(ttree.getLeftChild().getRightChild().getRootVal() =='d')
    print(ttree.getRightChild().getLeftChild().getRootVal() =='e')





    
            