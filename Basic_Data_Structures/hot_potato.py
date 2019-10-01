class Queue:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def show(self):
        print(self.items)

def hot_potato(names, num):
    q = Queue()

    # Add names to queue:
    for name in names:
        q.enqueue(name)
    
    t = 0
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        
        q.dequeue()

    return q.dequeue()

    

if __name__ == '__main__':
    names = ['Justin', 'Sam', 'Savannah', 'Ray', 'Kammi', 'Lindsay', 'Mike', 'Amanda', 'Laurie', 'Zach', 'Jennifer', 'Felix']
    names = ["Bill","David","Susan","Jane","Kent","Brad"]
    num = 7
    print(hot_potato(names,num))
