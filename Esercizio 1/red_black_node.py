from node import Node
from enum import Enum


class Color(Enum):
    """ Possible node colors """
    RED = True
    BLACK = False


class RedBlackNode(Node):
    """ Node of a Red Black Tree """

    def __init__(self, key: int):
        super().__init__(key)
        self.color = Color.RED
        self.parent = None
        self.left: RedBlackNode | None = None
        self.right: RedBlackNode | None = None
