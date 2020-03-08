#!python
from collections import deque


class BinaryTreeNode(object):
    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        def recur(node):
            return (max(
                recur(node.left) if node.left else 0,
                recur(node.right) if node.right else 0)) + 1

        return recur(self) - 1


class BinarySearchTree(object):
    def __init__(self, items=None, use_recursive=False):
        """Initialize this binary search tree and  the given items."""
        self.use_recursive = use_recursive
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = (self._find_node_recursive(item, self.root)
                if self.use_recursive else self._find_node_iterative(item))
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = (self._find_node_recursive(item, self.root)
                if self.use_recursive else self._find_node_iterative(item))
        return None if node is None else node.data

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find the parent node of where the given item should be inserted
        parent = (self._find_parent_node_recursive(item, self.root)
                  if self.use_recursive else
                  self._find_parent_node_iterative(item))

        if self.root is not None and parent is None:
            print(item, self.root.data, self.root.left, self.root.right)
            #assert self.root.left is self.root.right is None
            parent = self.root

        if self.is_empty():
            ## Tree is empty
            self.root = BinaryTreeNode(item)
        else:

            if item in map(lambda node: node.data,
                           filter(lambda node: node is not None,
                                  (parent, parent.left, parent.right))):
                ## This item is a duplicate, exit early
                print('duplicate')
                return
            if item < parent.data:
                ## Node should be to the left of parent
                parent.left = BinaryTreeNode(item)
            elif item > parent.data:
                ## Node should be to the right of parent
                parent.right = BinaryTreeNode(item)
        self.size += 1

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def is_root(self, node):
        return node is self.root

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root

        while node is not None:
            ## Loop until we descend past the closest leaf node
            if node.data == item:
                # Return the found node
                return node
            elif item < node.data:
                node = node.left
            else:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data == item:
            # Return the found node
            return node
        elif node.data < item:
            return self._find_node_recursive(item, node.right)
        return self._find_node_recursive(item, node.left)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            ## Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            parent = node

            if item < node.data:
                node = node.left
            else:
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None or item == node.data:
            ## Not found (base case) or the given item matches the node's data
            return parent
        elif item < node.data:
            ## The given item is left of node
            return self._find_parent_node_recursive(item,
                                                    node.left,
                                                    parent=node)
        ## The given item is right of node
        return self._find_parent_node_recursive(item, node.right, parent=node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        node = self._find_node_iterative(item)
        parent = self._find_parent_node_iterative(item)
        if self.is_leaf(node):
            ## No children; item is leaf
            if self.is_root(node):
                ## Check if root
                self.root = None
            else:
                if item < parent.data:
                    ## Check if parent is greater
                    parent.left = None
                else:
                    ## Parent is less
                    parent.right = None
        elif node.left is not None and node.right is None:
            ## One direct child on the left
            child = node.left
            parent.left = child
        elif node.left is None and node.right is not None:
            ## One direct child on the right
            child = node.right
            parent.left = child
        else:
            ## Two direct children
            ## Find successor and swap with item
            child = node.right
            leftmost = child

            while leftmost.left is not None:
                leftmost = leftmost.left

            if item < parent.data:
                parent.left = leftmost
            else:
                parent.right = leftmost
            leftmost.left = node.left


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # (self._traverse_in_order_recursive(self.root, items.append)
            #  if self.use_recursive else self._traverse_in_order_iterative(
            #      self.root, items.append))
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # queue = deque([node])
        #
        # while len(queue):
        #     cur_node = queue.popleft()
        #
        #     if cur_node.left is not None:
        #         queue.append(cur_node.left)
        #     visit(cur_node.data)
        #
        #     if cur_node.right is not None:
        #         queue.append(cur_node.right)
        # for level in self._levels(node):
        #     for node in level:
        #         visit(node.data)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        queue = deque([start_node])
        while len(queue):
            node = queue.popleft()
            if node is not None:
                visit(node.data)
                queue.extend([node.left, node.right])

    def levels(self):
        return self._levels(self.root)

    def _levels(self, node):
        levels = []
        level = deque([(node, 0)])

        while len(level):
            cur_node, cur_level = level.popleft()

            if len(levels) <= cur_level:
                ## This is a new level in tree
                levels.append([cur_node])
            else:
                ## This is a previously-visited level in tree
                levels[-1].append(cur_node)
            level.extend((
                ([(cur_node.left, cur_level + 1)] if cur_node.left else []) +
                ([(cur_node.right, cur_level + 1)] if cur_node.right else [])))
            print(level)
        return levels

    def __str__(self):
        # return '\n'.join(map(lambda level: ' '.join(map(lambda node: str(node.data), level)), self.levels()))
        return '\n'.join(map(str, self.levels()))

    def __eq__(self, other):
        return (self.items_in_order() == other.items_in_order())


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
