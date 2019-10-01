class Stack:

    def __init__(self):
        # Create an empty list for storage of stack
        self.items = []
    
    def size(self):
        # Return the size (number of items) in the stack (items list)
        return len(self.items)
    
    def isEmpty(self):
        # Return boolean to check if the stack is empty
        return self.items == []

    def push(self, item):
        # Add an item to the stack. Returns nothing
        self.items.append(item)

    def pop(self):
        # Pop item off top of stack
        return self.items.pop()

    def peek(self):
        # return the top item on the stack, but don't pop it
        return self.items[len(items) - 1]

# Function to specifically convert decimal to binary
def divide_by_2(decimal):
    remainder_stack = Stack()

    # Add reaminder of decimal // 2 to stack until 0
    while decimal > 0:
        remainder_stack.push(decimal % 2)
        decimal //= 2

    # Pop items off stack to produce binary string
    binary_string = ''
    while not remainder_stack.isEmpty():
        binary_string = binary_string + str(remainder_stack.pop())

    return binary_string

# Generalized function to convert decimal to anything upto base 16
def base_converter(decimal, base):
    digits ='0123456789ABCDEF'

    remainder_stack = Stack()
    
    # Add reaminder of decimal to stack until 0
    while decimal > 0:
        remainder_stack.push(decimal % base)
        decimal //= base

    # Pop items off stack to produce base string
    base_string = ''
    while not remainder_stack.isEmpty():
        base_string += digits[remainder_stack.pop()]

    return base_string

if __name__ == '__main__':
    dec = int(input('Enter decimal: '))
    base = int(input('Enter base: '))
    #print(divide_by_2(dec))
    print(base_converter(dec, base))