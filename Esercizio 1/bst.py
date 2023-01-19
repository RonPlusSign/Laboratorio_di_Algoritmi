from node import Node


class BST:
    """ Binary Search Tree """

    def __init__(self):
        """ Constructor """
        self.root = None

    def set_root(self, key):
        """ Set the root  of the tree """
        self.root = Node(key)

    def insert(self, key):
        """ Insert a new key into the tree """
        if (self.root is None):
            self.set_root(key)
        else:
            self.insert_node(self.root, key)

    def insert_node(self, current_node: Node, key: int):
        """ Find the correct position for the key and insert a new node into the tree """
        if (key <= current_node.key):
            if (current_node.left):
                self.insert_node(current_node.left, key)
            else:
                current_node.left = Node(key)
        elif (key > current_node.key):
            if (current_node.right):
                self.insert_node(current_node.right, key)
            else:
                current_node.right = Node(key)

    def find(self, key):
        """
        Check if the given key exists in the tree
        :return true if the given key exists in the tree, false otherwise
        """
        return self.find_node(self.root, key)

    def find_node(self, current_node, key):
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

    def inorder(self):
        """ Inorder tree walk. Print the nodes in order """

        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print(v.key)
            if (v.right is not None):
                _inorder(v.right)

        _inorder(self.root)


def main():
    """ Test the Binary Search Tree """
    tree = BST()
    tree.insert(4)
    tree.insert(5)
    for x in range(20, 10, -1):
        tree.insert(x)

    print(tree.find(5))
    print(tree.find(2))
    tree.inorder()


if __name__ == "__main__":
    main()
