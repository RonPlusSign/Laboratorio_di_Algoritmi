class Node:
    """ Node of a Binary Search Tree """

    def __init__(self, key: int):
        """ Constructor """
        self.key = key
        self.left = None
        self.right = None

    def get(self):
        """ Get the node key """
        return self.key

    def set(self, key: int):
        """" Set the node key"""
        self.key = key

    def get_children(self):
        """"
        Recursively get the list of all children of the node
        :return array<Node> list of all Node children
        """
        children = []
        if (self.left is not None):
            children.append(self.left)
        if (self.right is not None):
            children.append(self.right)
        return children
