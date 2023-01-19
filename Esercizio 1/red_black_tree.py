from red_black_node import RedBlackNode, Color
from binary_search_tree import BST


class RBT(BST):
    """
    Red Black Tree

    """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.root: RedBlackNode | None = None

    def left_rotate(self, node: RedBlackNode):
        """
        Left rotate the tree, starting from the given node
        :param node: root of the rotation (will be moved left, and its right child takes its place)
        """
        replacer = node.right
        node.right = replacer.left

        # Update replacer left child (its parent now should be the given node)
        if replacer.left is not None:
            replacer.left.parent = node

        replacer.parent = node.parent  # Update replacer parent

        # Update starting node parent
        if node.parent is None:  # Node was root
            self.root = replacer
        elif node == node.parent.left:  # Node was the left child
            node.parent.left = replacer
        else:  # Node was the right child
            node.parent.right = replacer

        # Set relationship between the given node and the replacer
        replacer.left = node
        node.parent = replacer

    def right_rotate(self, node: RedBlackNode):
        """
        Right rotate the tree, starting from the given node
        :param node: root of the rotation (will be moved right, and its left child takes its place)
        """
        replacer = node.left
        node.left = replacer.right

        # Update replacer right child (its parent now should be the given node)
        if replacer.right is not None:
            replacer.right.parent = node

        replacer.parent = node.parent  # Update replacer parent

        # Update starting node parent
        if node.parent is None:  # Node was root
            self.root = replacer
        elif node == node.parent.left:  # Node was the left child
            node.parent.left = replacer
        else:  # Node was the right child
            node.parent.right = replacer

        # Set relationship between the given node and the replacer
        replacer.right = node
        node.parent = replacer

    def set_root(self, key: int):
        """ Set the root of the tree """
        self.root = RedBlackNode(key)

    def insert(self, key: int):
        """ Insert a node inside the tree """

        if (self.root is None):
            self.set_root(key)
        else:
            new_node = RedBlackNode(key)
            super().insert_node(self.root, new_node)
            self.insert_fixup(new_node)

    def insert_fixup(self, node: RedBlackNode):
        """ Fix the red black tree properties after a node inserting """
        while node.parent is not None and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:  # Parent is the left child
                y = node.parent.parent.right  # Uncle node
                if y.color == Color.RED:  # Case 1: uncle is red
                    node.parent.color = Color.BLACK
                    node.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:  # Uncle is black
                    if node == node.parent.right:  # Case 2: uncle is black, and it's the right child. Adjust to get to case 3
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = Color.BLACK  # Case 3: uncle is black, and it's the left child
                    node.parent.parent.color = Color.RED
                    self.right_rotate(node.parent.parent)
            else:  # Parent is the right child
                y = node.parent.parent.left  # Uncle node
                if y.color == Color.RED:  # Case 1: uncle is red
                    node.parent.color = Color.BLACK
                    node.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:  # Uncle is black
                    if node == node.parent.left:  # Case 2: uncle is black, and it's the left child. Adjust to get to case 3
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = Color.BLACK  # Case 3: uncle is black, and it's the right child
                    node.parent.parent.color = Color.RED
                    self.left_rotate(node.parent.parent)
        self.root.color = Color.BLACK


def main():
    """ Test the Red Black Tree """
    from draw_tree import print_rb_tree
    from random import randint

    tree = RBT()
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
    print_rb_tree(tree)


if __name__ == "__main__":
    main()