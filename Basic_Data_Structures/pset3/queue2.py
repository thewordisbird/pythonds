# It is possible to implement a queue such that both enqueue and dequeue have 
# O(1) performance on average. In this case it means that most of the time enqueue 
# and dequeue will be O(1) except in one particular circumstance where dequeue will be O(n).

# Yes! By using a linked list that maintains it's start and end node instead of a list we can achieve this

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def setNext(self, next_node):
        self.next = next_node
    
    def setPrevious(self, previous_node):
        self.previous = previous_node

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''Adds item to back (right side) of LinkedList'''
        n = Node(data)
        if self.head == None:
            self.head = self.tail = n
        else:
            self.tail.setNext(n)
            n.setPrevious(self.tail)
            self.tail = n

    def append_left(self, data):
        '''Adds item to front (left side) of LinkedList'''
        n = Node(data)
        if self.head == None:
            self.head = self.tail = n
        else:
            n.setNext = self.head
            self.head.setPrevious(n)
            self.head = n

    def pop(self):
        '''Removes and returns item from back (right side) of LinkedList'''
        n = self.tail
        self.tail = n.getPrevious()
        self.tail.setNext(None)
        return n.getData()

    def pop_left(self):
        '''Removes and returns item from front (left side) of LinkedList'''
        n = self.head
        self.head = n.getNext()
        self.head.setPrevious(None)
        return n.getData()


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop_left()  


