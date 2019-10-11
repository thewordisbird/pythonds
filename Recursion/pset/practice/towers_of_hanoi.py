# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.

def hanoi(n, s, t, a):
    '''Recursively solves tower of hanoi problem.
            n: number of disk (int number of disk)
            s: start location (string description of location)
            t: target location (string description of location)
            a: aux location (string description of location)
       Prints steps to solve puzzel'''
    # Set base case
    if n == 1:
        print(f'Move disk from {s} to {t}')
    else:
        # Move stack of n-1 to aux to allow movement of bottom disk from start to target
        hanoi(n-1,s,a,t)
        # Print step to move bottom disk to target:
        print(f'Move disk from {s} to {t}')
        # Move remainder of stack to target
        hanoi(n-1, a, t, s)

if __name__ == '__main__':
    disks = 3
    hanoi(disks, 'Pole A', 'Pole C', 'Pole B')