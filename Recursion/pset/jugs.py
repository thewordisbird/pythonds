# You have two jugs: a 4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on them. 
# There is a pump that can be used to fill the jugs with water. How can you get exactly two gallons 
# of water in the 4-gallon jug?

class Jug:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.volume = 0

    def fill(self):
        print(f'Fill {self.name} with {self.capacity}')
        self.volume = self.capacity

    def transfer(self, to_jug):
        avil_transfer_capacity = to_jug.get_capacity() - to_jug.get_volume()
        print(f'Transfer {self.volume} from {self.name} to {to_jug.get_name()} ')
        if self.volume < avil_transfer_capacity:
            
            to_jug.set_volume(self.volume)
            self.volume = 0
        else:
            self.volume = self.volume - avil_transfer_capacity
            to_jug.set_volume(to_jug.get_capacity())
    
    def dump(self):
        print(f'Empty {self.name}')
        self.volume = 0
    
    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_volume(self):
        return self.volume

    def set_volume(self, amt):
        self.volume = amt
    
    

if __name__ == '__main__':
    size_big_jug = input('Enter size of larger jug: ')
    size_small_jug = input('Enter size of smaller jug: ')
    
    big_jug = Jug(size_big_jug + ' Gal Jug', int(size_big_jug))
    small_jug = Jug(size_small_jug + ' Gal Jug', int(size_small_jug))
    
    
    big_jug.fill()
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')
    print('\n')
    
    big_jug.transfer(small_jug)
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')
    print('\n')

    small_jug.dump()
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')
    print('\n')
    
    big_jug.transfer(small_jug)
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')
    print('\n')

    big_jug.fill()
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')
    print('\n')
    
    big_jug.transfer(small_jug)
    print(f'{big_jug.get_name()}: {big_jug.get_volume()} | {small_jug.get_name()}: {small_jug.get_volume()} ')