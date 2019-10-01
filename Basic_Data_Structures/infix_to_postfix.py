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







def infix_to_postfix(infix_expression):
    infix = validate_infix(infix_expression)
    predence = {'**': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(':1}
    operand = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    opstack = Stack()
    postfix_list = []

    token_list = infix.split()

    for token in token_list:
        if token in operand:
            postfix_list.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (predence[opstack.peek()] >= predence[token]):
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())

    return " ".join(postfix_list)

def evaluate_postfix(postfix_expression):
    operands = "0123456789"
    operand_stack = Stack()
    postfix_list = postfix_expression.split(" ")

    for i in postfix_list:
        if i in operands:
            operand_stack.push(int(i))
        else:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            result = do_math(i, operand_1, operand_2)
            operand_stack.push(result)
    
    return operand_stack.pop()

def do_math(operator, operand_1, operand_2):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    else:
        return operand_1 / operand_2

def validate_infix(infix_expression):
    ''' Makes sure there are only valid characters and
        every character has a space between them '''
    valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()+-*/'
    # This will remove any spaces. They will be
    # re-implemented with a join() at the end
    infix = infix_expression.upper().split()
    for c in infix:
        if c == '**':
            pass
        elif c not in valid_chars:
            raise TypeError(f'Invalid Character: {c}')
    return " ".join(infix)

if __name__ == '__main__':
    print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))
    #print(infix_to_postfix("( A ! B ) * C - ( D - E ) * ( F + G )"))

    #print(evaluate_postfix('7 8 + 3 2 + /'))