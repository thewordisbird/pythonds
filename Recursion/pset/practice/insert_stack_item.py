# Recursively insert an item at the beginning of the stack.
# There are 2 solutions presented here:
#   1. create an insert method in the Stack class that will recursively insert the item at the bottom of the stack
#       storing the top items in the call stack as a means of temporary storage.
#   2. creates a seperate function to insert and item in the stack. This was just to confirm that it would work the 
#       same and not other temp variables would need to be created to make it function properly

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def insert(self, item):
        if self.isEmpty():
            return self.push(item)
        
        else:
            top_item = self.pop()
            self.insert(item)
            return self.push(top_item)


def insert_item(stack, item):
    if stack.isEmpty():
        return stack.push(item)
    else:
        top_item = stack.pop()
        insert_item(stack, item)
        return stack.push(top_item)
            

if __name__ == '__main__':
    s = Stack()
    # Load stack with 3 items
    for i in range(3):
        s.push(i)
    print(s.items)
    
    # Insert item -1 at front of stack with class method
    s.insert(-1)
    print(s.items)

    # Insert item -2 at front of stack using insert_item function
    insert_item(s, -2)
    print(s.items)

    