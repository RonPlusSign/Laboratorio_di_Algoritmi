from linked_list import LinkedListQueue, LinkedListNode


class SortedLinkedListQueue(LinkedListQueue):
    """ Class that represents a Queue implemented with a sorted linked list.
    It extends the LinkedListQueue class, so that the elements are always sorted by value in descending order.
    The maximum value is always the first element of the queue (head), and the minimum value is always the last element (tail).
    """

    def __init__(self):
        super().__init__()

    def insert(self, value):
        """ Insert a new node in the queue in the correct position """
        new_node = LinkedListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None and current_node.value > value:
                previous_node = current_node
                current_node = current_node.next

            if previous_node is None:
                self.head = new_node
                new_node.next = current_node
            else:
                previous_node.next = new_node
                new_node.next = current_node

            if current_node is None:
                self.tail = new_node

    def find_max(self):
        """ Return the node with the maximum value """
        return self.head

    def extract_max(self):
        """ Delete and return the node with the maximum value """
        if self.is_empty():
            return None
        else:
            max_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return max_node


if __name__ == '__main__':
    queue = SortedLinkedListQueue()

    queue.insert(2)
    queue.insert(9)
    queue.insert(4)
    queue.insert(3)
    queue.insert(7)

    print(queue)  # 9->7->4->3->2
    print(queue.find_max())  # Node(9)
    print(queue.extract_max())  # Node(9)
    print(queue)  # 7->4->3->2

    # Insert 100 random values in the queue
    import random
    for _ in range(100):
        queue.insert(random.randint(0, 100))
        
    print(queue)
    print('Extract max: ', queue.extract_max())
    print(queue)