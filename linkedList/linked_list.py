class Node:
    """A single node in a singly linked list."""

    def __init__(self, data):
        """Initialise node with data and no next pointer.

        Args:
            data: The value stored in this node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list with optional reversal support."""

    def __init__(self):
        """Initialise an empty linked list."""
        self.head = None

    def append(self, data):
        """Append a new node with data to the end of the list.

        Args:
            data: The value to append.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Insert a new node with data at the front of the list.

        Args:
            data: The value to prepend.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove the first node containing data.

        Does nothing if data is not found.

        Args:
            data: The value to remove.
        """
        if self.head is None:
            return
        # Head node is the target
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        """Reverse the linked list in place.

        Iterates through the list, flipping each next pointer so the
        list is reversed without allocating new nodes.

        >>> ll = LinkedList()
        >>> ll.append(1); ll.append(2); ll.append(3)
        >>> ll.reverse()
        >>> ll.to_list()
        [3, 2, 1]
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next  # save next
            current.next = prev       # reverse pointer
            prev = current            # advance prev
            current = next_node       # advance current
        self.head = prev

    def to_list(self):
        """Return all node values as a Python list.

        Returns:
            A list of node data values in order.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        """Return a string representation of the list."""
        nodes = self.to_list()
        if not nodes:
            return "None"
        return " -> ".join(str(x) for x in nodes) + " -> None"
