
def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1,[newBranch, t, []])
    else:
        root.insert(1,[newBranch, [], []])
    return root
                       
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2,[newBranch, t, []])
    else:
        root.insert(2,[newBranch, [], []])
    return root 
     
def getRootVal(root):
    return root[0]
                                       
def setRootVal(root, newVal):
    root[0] = newVal
                                        
def getLeftChild(root):
    return root[1]
                                
def getRightChild(root):
    return root[2]
    
                    
def buildTree():
    t = BinaryTree('a')

    insertLeft(t, 'b')
    insertRight(t, 'c')

    insertRight(getLeftChild(t), 'd')
    insertLeft(getRightChild(t), 'e')
    insertRight(getRightChild(t), 'f')
    return t

ttree = buildTree()
print(ttree)
print(getRootVal(getRightChild(ttree)) == 'c')
print(getRootVal(getRightChild(getLeftChild(ttree))) == 'd')
print(getRootVal(getRightChild(getRightChild(ttree))) == 'f')
