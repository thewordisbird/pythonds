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

class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp

    def remove(self, target):
        current = self.head
        previous = None

        while current != None:
            if current.getData() == target:
                if previous == None and current.getNext() == None:
                    self.head = None
                elif previous == None and current.getNext() != None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
            previous = current
            current = current.getNext()
            

    def size(self):
        current = self.head
        count = 0

        while current !=None:
            count += 1
            current = current.getNext()
        
        return count

    def isEmpty(self):
        return self.head == None

    def search(self, target):
        current = self.head
        while current != None:
            if current.getData() == target:
                return True
            current = current.getNext()
        return False


    def append(self, data):
        temp = Node(data)
        
        if self.head == None:
            self.head = temp
            return
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            
            current.setNext(temp)
    


class UnorderedList_1:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            temp.setNext(self.head)
            self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        
        return count
            
    def remove(self, target):
        current = self.head
        previous = None

        while current != None:
            if current.getData() == target:
                if previous == None and self.tail == current:
                    self.head = None
                    self.tail = None
                elif previous == None and self.tail != None:
                    self.head = current.getNext()
                elif current == self.tail:
                    previous.setNext(None)
                    self.tail = previous
                else:
                    previous.setNext(current.getNext())
            previous = current
            current = current.getNext()

    def isEmpty(self):
        return self.head == None

    def search(self, target):
        current = self.head
        while current != None:
            if current.getData() == target:
                return True
            current = current.getNext()

    def append(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.setNext(temp)
            self.tail = temp
                    
        

