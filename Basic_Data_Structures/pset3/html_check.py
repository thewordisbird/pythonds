# Problem:
# Another example of the parentheses matching problem comes from hypertext markup language (HTML). 
# In HTML, tags exist in both opening and closing forms and must be balanced to properly describe 
# a web document. This very simple HTML document:

# <html>
#    <head>
#       <title>
#          Example
#       </title>
#    </head>

#    <body>
#       <h1>Hello, world</h1>
#    </body>
# </html>

# is intended only to show the matching and nesting structure for tags in the language. Write a program 
# that can check an HTML document for proper opening and closing tags.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(len(self.items) - 1)

    def isEmpty(self):
        return self.items == []


def html_check(doc_path):
    tag_stack = Stack()
    
    with open(doc_path) as f:
        html_file = f.read()

    for c in html_file:
        if c == '<':
            tag_stack.push(c)
        elif c == '>':
            if tag_stack.pop() != '<':
                return False

    if tag_stack.isEmpty():
        return True
    else:
        return False