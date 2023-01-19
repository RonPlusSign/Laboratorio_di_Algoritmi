from typing import Callable
from node import Node

class BST:
    """ Binary Search Tree """

    def __init__(self):
        """ Constructor """
        self.root: Node | None = None

    def set_root(self, new_root: Node):
        """ Set the root  of the tree """
        self.root = new_root

    def insert(self, key: int):
        """ Insert a new key into the tree """
        if self.root is None:
            self.set_root(Node(key))
        else:
            self.insert_node(self.root, Node(key))

    def insert_node(self, current_node: Node, new_node: Node):
        """ Find the correct position for the key and insert a new node into the tree """
        if (new_node.key <= current_node.key):
            if (current_node.left):
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif (new_node.key > current_node.key):
            if (current_node.right):
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    def find(self, key: int):
        """
        Check if the given key exists in the tree
        :return true if the given key exists in the tree, false otherwise
        """
        return self.find_node(self.root, key)

    def find_node(self, current_node: Node | None, key: int):
        """
        Recursively search if there's a node with the given key
        :return true if the given key exists in the tree, false otherwise
        """
        if (current_node is None):
            return False
        elif (key == current_node.key):
            return True
        elif (key < current_node.key):
            return self.find_node(current_node.left, key)
        else:
            return self.find_node(current_node.right, key)

    def inorder_walk(self, node: Node, callback: Callable[[Node], None]):
        """ Inorder tree walk
        Execute the callback for each of the nodes in order
        :parameter node: root from which to start the tree walk
        :parameter callback: function to call for each node
        """
        if (node is None):
            return
        if (node.left is not None):
            self.inorder_walk(node.left, callback)
        callback(node)
        if (node.right is not None):
            self.inorder_walk(node.right, callback)

    def preorder_walk(self, node: Node, callback: Callable[[Node], None]):
        """ Preorder tree walk
        Execute the callback for each of the nodes. First the parent, then its children
        :parameter node: root from which to start the tree walk
        :parameter callback: function to call for each node
        """
        callback(node)
        if (node is None):
            return
        if (node.left is not None):
            self.preorder_walk(node.left, callback)
        if (node.right is not None):
            self.preorder_walk(node.right, callback)

    def postorder_walk(self, node: Node, callback: Callable[[Node], None]):
        """ Postorder tree walk
        Execute the callback for each of the nodes. First the children, then the parent
        :parameter node: root from which to start the tree walk
        :parameter callback: function to call for each node
        """
        if (node is None):
            return
        if (node.left is not None):
            self.postorder_walk(node.left, callback)
        if (node.right is not None):
            self.postorder_walk(node.right, callback)
        callback(node)


def main():
    """ Test the Binary Search Tree """
    from draw_tree import print_tree
    from random import randint

    tree = BST()
    # tree.insert(4)
    # tree.insert(5)
    # for x in range(50, 10, -1):
    #     tree.insert(x)

    for _ in range(100):
        number = randint(1, 200)
        if not tree.find(number):
            tree.insert(number)

    print(tree.find(5))
    print(tree.find(2))
    print_tree(tree)


if __name__ == "__main__":
    main()
