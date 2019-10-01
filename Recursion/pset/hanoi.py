# implement a solution to the Tower of Hanoi using three stacks to keep track of the disks

class Stack():
    def __init__(self, name):
        self.items = []
        self.name = name

    def get_name(self):
        return self.name

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []


def stack_hanoi(disks, start_stack, end_stack, aux_stack):
    load_disks(disks, start_stack)
    
def load_disks(n, stack):
    for i in range(n, 0, -1):
        stack.push(i)

def rec_stack_hanoi(disks, start, end, aux):
    if disks == 1:
        end.push(start.pop())
        print(f'Move disk from {start.get_name()} to {end.get_name()} | {a.size()}, {b.size()}, {c.size()}')
    else:
        rec_stack_hanoi(disks - 1, start, aux, end)
        end.push(start.pop())
        print(f'Move disk from {start.get_name()} to {end.get_name()} | {a.size()}, {b.size()}, {c.size()}')
        rec_stack_hanoi(disks - 1, aux, end, start)

def rec_hanoi(disks, start, end, aux):
    if disks == 1:
        print(f'Move disk from {start} to {end}')
    else:
        rec_hanoi(disks - 1, start, aux, end)
        print(f'Move disk from {start} to {end}')
        rec_hanoi(disks - 1, aux, end, start)


if __name__ == '__main__':
    a = Stack('a')
    b = Stack('b')
    c = Stack('c')   
    load_disks(5, a)
    print('rec_hanoi')
    rec_hanoi(5, 'a', 'c', 'b')
    print('\nrec_stack_hanoi')
    rec_stack_hanoi(5, a, c, b)
