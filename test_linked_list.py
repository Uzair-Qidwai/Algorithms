import unittest
from linked_list import LinkedList, Node


class TestNode(unittest.TestCase):
    """Tests for the Node class."""

    def test_node_stores_data(self):
        node = Node(42)
        self.assertEqual(node.data, 42)

    def test_node_next_is_none(self):
        node = Node(1)
        self.assertIsNone(node.next)

    def test_node_next_can_be_set(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        self.assertEqual(n1.next.data, 2)


class TestLinkedListAppend(unittest.TestCase):
    """Tests for append()."""

    def test_append_to_empty(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.to_list(), [1])

    def test_append_multiple(self):
        ll = LinkedList()
        for val in [1, 2, 3]:
            ll.append(val)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_append_preserves_order(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        ll.append("c")
        self.assertEqual(ll.to_list(), ["a", "b", "c"])


class TestLinkedListPrepend(unittest.TestCase):
    """Tests for prepend()."""

    def test_prepend_to_empty(self):
        ll = LinkedList()
        ll.prepend(10)
        self.assertEqual(ll.to_list(), [10])

    def test_prepend_inserts_at_front(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(3)
        ll.prepend(1)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_prepend_multiple(self):
        ll = LinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        self.assertEqual(ll.to_list(), [1, 2, 3])


class TestLinkedListDelete(unittest.TestCase):
    """Tests for delete()."""

    def test_delete_only_element(self):
        ll = LinkedList()
        ll.append(1)
        ll.delete(1)
        self.assertEqual(ll.to_list(), [])

    def test_delete_head(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(1)
        self.assertEqual(ll.to_list(), [2, 3])

    def test_delete_middle(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(2)
        self.assertEqual(ll.to_list(), [1, 3])

    def test_delete_tail(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(3)
        self.assertEqual(ll.to_list(), [1, 2])

    def test_delete_nonexistent_is_safe(self):
        ll = LinkedList()
        ll.append(1)
        ll.delete(99)
        self.assertEqual(ll.to_list(), [1])

    def test_delete_on_empty_is_safe(self):
        ll = LinkedList()
        ll.delete(1)
        self.assertEqual(ll.to_list(), [])

    def test_delete_first_occurrence_only(self):
        ll = LinkedList()
        for v in [1, 2, 1, 3]:
            ll.append(v)
        ll.delete(1)
        self.assertEqual(ll.to_list(), [2, 1, 3])


class TestLinkedListReverse(unittest.TestCase):
    """Tests for reverse()."""

    def test_reverse_single_element(self):
        ll = LinkedList()
        ll.append(1)
        ll.reverse()
        self.assertEqual(ll.to_list(), [1])

    def test_reverse_two_elements(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.reverse()
        self.assertEqual(ll.to_list(), [2, 1])

    def test_reverse_multiple(self):
        ll = LinkedList()
        for v in [1, 2, 3, 4, 5]:
            ll.append(v)
        ll.reverse()
        self.assertEqual(ll.to_list(), [5, 4, 3, 2, 1])

    def test_reverse_empty_is_safe(self):
        ll = LinkedList()
        ll.reverse()
        self.assertEqual(ll.to_list(), [])

    def test_double_reverse_restores_order(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.reverse()
        ll.reverse()
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_reverse_does_not_create_new_nodes(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        original_head_data = ll.head.data
        ll.reverse()
        # Original head data should now be at the tail
        self.assertEqual(ll.to_list()[-1], original_head_data)


class TestLinkedListLen(unittest.TestCase):
    """Tests for __len__()."""

    def test_len_empty(self):
        self.assertEqual(len(LinkedList()), 0)

    def test_len_after_appends(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        self.assertEqual(len(ll), 3)

    def test_len_after_delete(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(2)
        self.assertEqual(len(ll), 2)


class TestLinkedListRepr(unittest.TestCase):
    """Tests for __repr__()."""

    def test_repr_empty(self):
        ll = LinkedList()
        self.assertEqual(repr(ll), "None")

    def test_repr_single(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(repr(ll), "1 -> None")

    def test_repr_multiple(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        self.assertEqual(repr(ll), "1 -> 2 -> 3 -> None")


if __name__ == "__main__":
    unittest.main(verbosity=2)
