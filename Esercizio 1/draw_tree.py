from treelib import Tree
from binary_search_tree import BST
from red_black_tree import RBT
from node import Node
from red_black_node import Color, RedBlackNode


def print_tree(tree: BST):
    if tree.root is None:
        return

    drawer = Tree()
    drawer.create_node(tree.root.key, tree.root.key)

    def add_node(node: Node):
        if node.left is not None:
            drawer.create_node(node.left.key, node.left.key, node.key)
        if node.right is not None:
            drawer.create_node(node.right.key, node.right.key, node.key)

    tree.preorder_walk(tree.root, add_node)
    drawer.show()


def print_rb_tree(tree: RBT):
    if tree.root is None:
        return

    drawer = Tree()
    drawer.create_node(tree.root.key, tree.root.key,
                       data=(str(tree.root.key) + " " + ("(red)" if tree.root.color == Color.RED else "(black)")))

    def add_node(node: Node | RedBlackNode):
        if node.left is not None:
            drawer.create_node(str(node.left.key) + " " + ("(red)" if node.left.color == Color.RED else "(black)"),
                               node.left.key, node.key)
        if node.right is not None:
            drawer.create_node(str(node.right.key) + " " + ("(red)" if node.right.color == Color.RED else "(black)"),
                               node.right.key, node.key)

    tree.preorder_walk(tree.root, add_node)
    drawer.show()
