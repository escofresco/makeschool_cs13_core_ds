import unittest

from binarytree import BinarySearchTree
from set import Set

class SetTest(unittest.TestCase):
    def test_eq_edges(self):
        assert Set() == BinarySearchTree()
        assert Set() == Set()
        assert Set([]) == Set()
        assert Set([]) == Set(())
        assert Set((1,1,1,1,1)) == Set((1,))

    def test_items_edges(self):
        assert Set((1,1,1,1,1,1,1)).items() == [1]
        assert Set((1,1,1,2,3,3,3,5,5)).items() == [1,2,3,5]

    def test_items(self):
        assert Set((3,)).items() == [3]
        assert Set((245234523452423452323,)).items() == [245234523452423452323]
        assert Set((3,2,1)).items() == [1,2,3]
        assert (Set(('zeitgeist', 'aardvark', 'camel')).items() ==
                ['aardvark', 'camel', 'zeitgeist'])

    def test_add(self):
        tiny_set = Set()
        tiny_set.add(3)
        assert tiny_set.items() == [3]
        assert tiny_set.data == BinarySearchTree((3,))

        tiny_set.add(2)
        assert tiny_set.items() == [2,3]
        assert tiny_set.data == BinarySearchTree((3,2))

        tiny_set.add(1)
        assert tiny_set.items() == [1,2,3]
        assert tiny_set.data == BinarySearchTree((3,2,1))

    def test_intersection(self):
        tiny_set = Set((1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))

        # Normal case
        assert tiny_set.intersection(big_set).items() == [1,2,3]
        assert big_set.intersection(other_big_set).items() == list(range(4, 100))

        # Check commutativity for normal case
        assert big_set.intersection(tiny_set).items() == [1,2,3]
        assert other_big_set.intersection(big_set).items() == list(range(4, 100))

        # Null case
        assert tiny_set.intersection(other_big_set).items() == []

    def test_difference(self):
        tiny_set = Set((0,1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))

        # Normal case
        assert big_set.difference(tiny_set).items() == list(range(4, 100))
        assert big_set.difference(other_big_set).items() == [0,1,2,3]

        # Check commutativity for normal case
        assert big_set.difference(tiny_set).items() == list(range(4, 100))

        # Null case
        assert other_big_set.difference(other_big_set).items() == []

    def test_union(self):
        tiny_set = Set((0,1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))

        # Normal case
        assert big_set.union(tiny_set).items() == list(range(100))
        assert big_set.union(other_big_set).items() == list(range(100))

        # Check commutativity for normal case
        assert tiny_set.union(big_set).items() == list(range(100))
        assert other_big_set.union(big_set).items() == list(range(100))

    def test_is_subset(self):
        tiny_set = Set((0,1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))

        # Normal case
        assert other_big_set.is_subset(big_set)
        assert tiny_set.is_subset(big_set)
        assert not tiny_set.is_subset(other_big_set)

    def test_contains(self):
        tiny_set = Set((0,1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))

        for i in range(4):
            assert tiny_set.contains(i)
            assert not other_big_set.contains(i)

        for i in range(100):
            assert big_set.contains(i)

        for i in range(4, 100):
            assert other_big_set.contains(i)
            assert not tiny_set.contains(i)

    def test_size(self):
        tiny_set = Set((0,1,2,3))
        big_set = Set(tuple(range(100)))
        other_big_set = Set(tuple(range(4, 100)))
        empty_set = Set()

        # Normal case
        assert tiny_set.size == 4
        assert big_set.size == 100
        assert other_big_set.size == 96

        # Null case
        assert empty_set.size == 0

    def test_remove(self):
        tiny_set = Set((0,1,2,3))

        tiny_set.remove(3)
        assert tiny_set.items() == [0,1,2]

        tiny_set.remove(2)
        assert tiny_set.items() == [0,1]
