# Implementation of minHeap following HackerRank class/method structure

# The important thing to remeber with a min or max heap is that it uses a simple list or array
# as the underlying data structure. The left child is at (2 * p) + 1 and the right child is at
# (2 * p) + 2. The parent of a child is at (c - 1) // 2. Using these relationships the rest of 
# the methods are mearly helpers. 
# 
# The only other considerations are heapify up and heapify down. The are used when adding or
# removing an item respectively. Using heapify down as an example, After the root is returned, the
# last element is moved to the root. At this point you find its smallest child and compare the 
# two. If the index element value is larger than the smallest child's value, you swap them until
# the heap is satisfied.

class MinHeap():
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(slef, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def get_left_child(self, index):
        return self.heap_list[self.get_left_child_index(index)]

    def get_right_child(self, index):
        return self.heap_list[self.get_right_child_index(index)]

    def get_parent(self, index):
        return self.heap_list[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        self.heap_list[index_one], self.heap_list[index_two] = self.heap_list[index_two], self.heap_list[index_one]
    
    def smaller_child_index(self, parent_index):
        left_child_index = self.get_left_child_index(parent_index)

    def peek(self):
        try:
            return self.heap_list[0]
        except:
            raise IndexError()

    def poll(self):
        print(self.heap_list)
        try:
            item = self.heap_list[0]
            self.heap_list[0] = self.heap_list[self.size - 1]
            self.size -= 1
            self.heapify_down()
            return item
        except:
            raise IndexError()

    def add(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index) > self.heap_list[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            
            if self.heap_list[index] < self.heap_list[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index
            
if __name__ == "__main__":
    nums = [5, 9, 14, 11, 17, 27, 18, 21, 33, 19]
    min_heap = MinHeap()

    for num in nums:
        min_heap.add(num)
    
    #print(min_heap.heap_list)

    print(min_heap.poll())
    print(min_heap.heap_list)
    




    