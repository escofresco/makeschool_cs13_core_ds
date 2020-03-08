"""This module is a custom implement of the set data type.

Implements:
    Set data type class."""
from binarytree import BinarySearchTree
from copy import deepcopy

class Set:
    """Implements a set using BinarySearchTree"""

    __slots__ = ("data",)

    def __init__(self, it=()):
        self.data = BinarySearchTree(it)

    def add(self, elm):
        self.data.insert(elm)

    def remove(self, elm):
        self.data.delete(elm)

    def union(self, other_set):
        bigger_set = max(self, other_set, key=lambda set: set.size)
        smaller_set = min(self, other_set, key=lambda set: set.size)
        return Set(self.items() + other_set.items())

    def intersection(self, other_set):
        bigger_set = max(self, other_set, key=lambda set: set.size)
        smaller_set = min(self, other_set, key=lambda set: set.size)
        return Set(tuple(elm for elm in smaller_set.items()
                         if bigger_set.contains(elm)))

    def difference(self, other_set):
        res = Set()
        for elm in self.items():
            if not other_set.contains(elm):
                res.add(elm)
        return res

    def is_subset(self, other_set):
        for elm in self.items():
            if not other_set.contains(elm):
                return False
        return True

    def items(self):
        return self.data.items_in_order()

    def contains(self, elm):
        return self.data.contains(elm)

    @property
    def size(self):
        return self.data.size

    def __eq__(self, other):
        if isinstance(other, BinarySearchTree):
            return self.data == other
        elif isinstance(other, Set):
            return self.data == other.data
        else:
            raise TypeError("Can only compare with BinarySearchTree and Set")
