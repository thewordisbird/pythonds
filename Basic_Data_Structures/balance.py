class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


def balance_char(str):
    s = Stack()
    d_chars = {'(': ')', '[': ']', '{':'}'}

    for i in str:
        if i in '({[':
            s.push(i)
        elif i != d_chars[s.pop()]:
            return False
    
    return True



if __name__ == '__main__':
    print(balance_char('{({([][])}())}'))
    print(balance_char('[{()]'))
