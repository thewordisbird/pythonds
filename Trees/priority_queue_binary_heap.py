# Implementation of Priority Queue with Binary Heap

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # Swap with parent
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            min_child = self.minChild(i)
            if self.heapList[i] > self.heapList[min_child]:
                self.heapList[i], self.heapList[min_child] = self.heapList[min_child], self.heapList[i]
            i = min_child

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            return i * 2 + 1

    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retVal
