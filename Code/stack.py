#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) since creating a pointer to the new item."""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        try:
            return self.list.get_at_index(0)
        except:
            pass

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) since deleting head."""
        if self.is_empty():
            raise ValueError("List is empty.")
        return self.list.pop_left()



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time:   O(1) amortized since more memory is occasionally
                        allocated."""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if len(self.list):
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time:   O(1) because deleting the last item from a list just
                        adds an extra spot to the right in memory."""
        if not self.length():
            raise ValueError("Stack is empty.")
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
