from queue import Queue


class LinkedListNode:
    """ Class that represents a node in a linked list """

    def __init__(self, val=0, next=None):
        self.value: int = val
        self.next: LinkedListNode | None = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedListQueue(Queue):
    """ Class that represents a Queue implemented with a linked list.
        A Queue is a data structure that follows the FIFO (First In First Out) principle.
        The maximum priority of the queue is the element with the maximum value.
    """

    def __init__(self):
        self.head: LinkedListNode | None = None
        self.tail: LinkedListNode | None = None

    def is_empty(self):
        return self.head is None

    def insert(self, value: int):
        """ Insert a new node at the end of the queue """
        new_node = LinkedListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_max(self):
        """ Get the node with the maximum value """
        if self.is_empty():
            return None
        else:
            current_node = self.head
            max_node = self.head
            while current_node is not None:
                if current_node.value > max_node.value:
                    max_node = current_node
                current_node = current_node.next
            return max_node

    def extract_max(self):
        """ Delete and return the node with the maximum value """
        if self.is_empty():
            return None
        elif self.head == self.tail:
            self.tail = None
            node = self.head
            self.head = None
            return node
        else:
            max_node = self.head
            max_node_prev = None
            current_node = self.head
            current_node_prev = None
            while current_node is not None:
                if current_node.value > max_node.value:
                    max_node = current_node
                    max_node_prev = current_node_prev
                current_node_prev = current_node
                current_node = current_node.next

            if max_node == self.head:  # max is the first node
                self.head = self.head.next
                return max_node
            elif max_node == self.tail:  # max is the last node
                self.tail = max_node_prev
                max_node_prev.next = None
                return max_node
            else:
                max_node_prev.next = max_node.next
                return max_node

    def __repr__(self):
        """ Return a string representation of the queue """
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return "->".join(nodes)


if __name__ == '__main__':
    queue = LinkedListQueue()

    queue.insert(2)
    queue.insert(9)
    queue.insert(4)
    queue.insert(3)
    queue.insert(7)

    print(queue)  # 2->9->4->3->7
    print(queue.find_max())  # Node(9)
    print(queue.extract_max())  # Node(9)
    print(queue)  # 2->4->3->7
    
    
    # Insert 100 random values in the queue
    import random
    for _ in range(100):
        queue.insert(random.randint(0, 100))
        
    print(queue)
    print('Extract max: ', queue.extract_max())
    print(queue)
