import math
from queue import Queue


class MaxHeap(Queue):
    """ Class for Max Heap data structure.
    A Max Heap is a semi-complete binary tree in which the value of each node is greater than or equal to the values in the children of that node.
    Root: node with the maximum value, which is the first element of the heap.
    Parent of i-th node: (i-1)//2 (integer division)
    Left child of i-th node: 2*i + 1
    Right child of i-th node: 2*i + 2
    """

    @staticmethod
    def left_child(index):
        return 2 * index + 1

    @staticmethod
    def right_child(index):
        return 2 * index + 2

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    def __init__(self):
        self.heap = []
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def max_heapify(self, index):
        """ Max-heapify the subtree rooted at index i """

        # Find max value between root element (i-th node) and its children
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index
        if left < self.size and self.heap[left] > self.heap[index]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        # Swap max value with root element (i-th node)
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)  # Max-heapify the subtree rooted at index largest

    def build_max_heap(self, array):
        """ Build a max heap from an array """
        self.heap = array
        self.size = len(array)
        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)

    def find_max(self):
        """ Return the root element (i.e. the maximum value) of the heap """
        if self.size == 0:
            return None
        else:
            return self.heap[0]

    def extract_max(self):
        """ Extract the root element (i.e. the maximum value) from the heap """
        if self.size == 0:
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.max_heapify(0)
        return max_value

    def increase_key(self, index, value):
        """ Increase the value of the i-th node to the given value """
        if value < self.heap[index]:
            return None

        self.heap[index] = value
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap i-th node with its parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def insert(self, value):
        """ Insert a new node in the heap """
        self.heap.append(-math.inf)
        self.size += 1
        self.increase_key(self.size - 1, value)

    def stringify_level(self, index, level):
        """ Return a string representation of the i-th node at the given level """
        if index >= self.size:
            return ''

        left = self.left_child(index)
        right = self.right_child(index)

        return ('   ' * (level - 1)) \
            + ('└──' if level > 0 else '') \
            + str(self.heap[index]) + "\n" \
            + (self.stringify_level(left, level + 1) if left < self.size else '') \
            + (self.stringify_level(right, level + 1) if right < self.size else '')

    def __repr__(self):
        """ Return a string representation of the heap """
        return self.stringify_level(0, 0)


if __name__ == '__main__':
    queue = MaxHeap()

    queue.insert(2)
    queue.insert(9)
    queue.insert(4)
    queue.insert(3)
    queue.insert(7)

    print(queue)
    print('Find max: ', queue.find_max())  # Node(9)
    print('Extract max: ', queue.extract_max())  # Node(9)
    print(queue)


    # Insert 100 random values in the heap
    import random
    for _ in range(100):
        queue.insert(random.randint(0, 100))
        
    print(queue)
    print('Extract max: ', queue.extract_max())
    print(queue)