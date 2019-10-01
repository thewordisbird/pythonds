class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

def pal_check(word):
    d = Dequeue()

    for l in word:
        d.addFront(l)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False
    
    return True

if __name__ == '__main__':
    word = 'rayar'
    print(word, pal_check(word))

    word = 'radar'
    print(word, pal_check(word))

