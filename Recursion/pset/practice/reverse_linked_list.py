# Recursively reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, next_node):
        self.next = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None    
        
    def addItem(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node

    def print_list(self):
        node = self.head
        while node.getNext() != None:
            print(node.getData())
            node = node.getNext()
        print(node.getData())

    def print_reversed(self, node=None):
        if node == None:
            node = self.head
        if node.getNext() == None:
            print(node.getData())
        else:
            self.print_reversed(node.getNext())
            print(node.getData())

    


if __name__ == '__main__':
    l = LinkedList()
    l.addItem('Justin')
    l.addItem('Lindsay')
    l.addItem('Amanda')
    l.addItem('Bosco')
    l.print_list()
    print('\n')
    print('Reversed')
    l.print_reversed()
    

