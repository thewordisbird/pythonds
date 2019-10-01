from collections import deque
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
        print(len(self.items) - 1)
        return self.items[len(self.items) - 1]
    
    def __str__(self):
        return repr(self.items)

def infix_to_postfix(infix_expression):
    infix = infix_expression.split()
    precedence = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    op_stack = Stack()
    postfix = []

    for c in infix:
        if c == '(':
            op_stack.push(c)
        elif c in precedence.keys() and not op_stack.isEmpty():
            while (not op_stack.isEmpty()) and precedence[c] < precedence[op_stack.peek()]:
                postfix.append(op_stack.pop())
            op_stack.push(c)
        elif c in precedence.keys():
            op_stack.push(c)
        elif c == ')':
            while op_stack.peek() != '(':
                postfix.append(op_stack.pop())
            op_stack.pop()
        else:
            postfix.append(c)
        print(postfix, op_stack)
    
    while op_stack.isEmpty() != True:
        postfix.append(op_stack.pop())
    print(f'Final Postfix: {" ".join(postfix)}')
    return ' '.join(postfix)


        