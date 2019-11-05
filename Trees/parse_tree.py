import operator

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


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
    
    def setRootVal(self, obj):
       self.key = obj

    def getRootVal(self):
        return self.key


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStatck = Stack()
    eTree = BinaryTree('')
    pStatck.push(eTree)
    currentTree = eTree
    operators = ['+', '-', '*', '/']
    
    for i in fplist:  
             
        if i == '(':
            # Add new node as the left child to the current node
            currentTree.insertLeft('')
            # Decend to left child node
            pStatck.push(currentTree)            
            currentTree = currentTree.getLeftChild()

        elif i in operators:
            # Set root val of current node to operator
            currentTree.setRootVal(i)
            # Add a new node as the right child of the current node
            currentTree.insertRight('')
            # Decend to right child
            pStatck.push(currentTree)
            currentTree = currentTree.getRightChild()
        
        elif i == ')':
            # Goto parent of the current node
            currentTree = pStatck.pop()

        elif i not in operators:
            try:
                currentTree.setRootVal(int(i))
                parent = pStatck.pop()
                currentTree = parent
            
            except ValueError:
                raise ValueError(f'Token {i} is not a valid integer')
    return eTree

def evaluate(parseTree):
    '''Recuresive evaluation of Binary tree for arthmetic'''
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()

    # Check for base case... leaf. A node with no children
    if leftChild and rightChild:
        fn = operators[parseTree.getRootVal()]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return parseTree.getRootVal()

if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))