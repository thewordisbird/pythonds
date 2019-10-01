# display steps to solve Tower of Hanoi problem for n disk

def tower(disks, start_pole, end_pole, aux_pole):
    if disks > 1:
        # move substack of disks-1 to the aux pole to free lowest remaining disk
        tower(disks -1, start_pole, aux_pole, end_pole)
        # move the newly freed disk to its destination
        print(f'move disk from {start_pole} to {end_pole}')
        # move the substack to the destination
        tower(disks-1, aux_pole, end_pole, start_pole)
    else:
        # This is only enacted for the first disk in each stack. 
        # otherwise the 'freed' disks are moved in the step above
        print(f'move disk from {start_pole} to {end_pole} -- called')

if __name__ == '__main__':
    disks = 4
    tower(disks, 'A', 'B', 'C')