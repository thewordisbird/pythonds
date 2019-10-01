def infix_to_prefix(infix_expression):
    infix = infix_expression.split()
    precedence = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    prefix = deque()
    temp = []

    for c in infix: