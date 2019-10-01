# Stack class implementation
class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


# Queue class implementation
class Queue:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

# Dequeue class implementation
class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Unordered (linked list) implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_list(self):
        current = self.head
        print('PRINTING LIST')
        while current != None:
            print(current.getData(), current.next)
            current = current.next


    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail is None:
            self.tail = temp
        self.head = temp
        print(self.head.getData(), self.tail.getData())

    def append(self, item):
        new_node = Node(item)

        # If list is empty make new node
        if self.head is None:
            self.head = self.tail = new_node            
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(item)
        self.tail = new_node

        print(self.head.getData(), self.tail.getData())
    
    def append_1(self, item):
        new_node = Node(item)

        # If list is empty make new node
        if self.head is None:
            self.head = self.tail = new_node            
            return

        temp = Node(item)
        print(f'self.tail= {self.tail.getData()} | self.tail.next = {self.tail.getNext()}')
        self.tail.setNext(temp)
        print(f'self.tail= {self.tail.getData()} | self.tail.next = {self.tail.getNext()}')
        self.tail = temp
        print(f'self.tail= {self.tail.getData()} | self.tail.next = {self.tail.getNext()}')
        
        print(self.head.getData(), self.tail.getData())
        


    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
            else:
                previous = current
                current = current.getNext()

ml = UnorderedList()
print('ADDING "Justin"')
ml.add('Justin')
ml.print_list()
print(ml.size())

print('APPENDING "amanda"')
ml.append('amanda')
ml.print_list()
print(ml.size())

print('APPENDING_1 "Lindsay"')
ml.append_1('Lindsay')
ml.print_list()
print(ml.size())

class Node:
'''Node class for items in an unordered singly linked list. The node contains the 
    data to be stored and a pointer to the next node in the list, which is initially
    set to None. It contins methods to get and set both attributes'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

class UnorderedList_1:

    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0

        while current !=None:
            count += 1
            current = current.getNext()
        
        return count

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
