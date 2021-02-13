import unittest

from random import randint
from linkedList2 import Node, LinkedList2


class add_in_tail(unittest.TestCase):
    def test_add_in_tail(self):
        s_list = LinkedList2()

        #add in empty list
        s_list.add_in_tail(Node(4))
        self.assertEqual(s_list.find(4).value, 4)
        self.assertEqual(s_list.head.value, 4)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.tail.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 1)

        #add in non empty list
        s_list.add_in_tail(Node(8))
        self.assertEqual(s_list.find(8).value, 8)
        self.assertEqual(s_list.head.value, 4)
        self.assertEqual(s_list.tail.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.tail.prev.value, 4)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 2)

        #add in non empty list
        s_list.add_in_tail(Node(11))
        self.assertEqual(s_list.find(11).value, 11)
        self.assertEqual(s_list.head.value, 4)
        self.assertEqual(s_list.tail.value, 11)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.tail.prev.value, 8)
        self.assertEqual(s_list.tail.next, None)

        self.assertEqual(s_list.find(8).prev.value, 4)
        self.assertEqual(s_list.find(8).next.value, 11)
        self.assertEqual(s_list.len(), 3)

        #check len after add Node(0) in empty list
        s_list = LinkedList2()
        s_list.add_in_tail(Node(0))
        s_list.len()
        self.assertEqual(s_list.len(), 1)
        self.assertNotEqual(s_list.len(), 0)
        self.assertEqual(s_list.find(0).value, 0)


class insert(unittest.TestCase):
    def test_insert(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))

        #insert in middle of list
        s_list.insert(Node(2), Node(3))
        self.assertEqual(s_list.find(3).value, 3)
        self.assertEqual(s_list.find(3).next.value, 4)
        self.assertEqual(s_list.find(3).prev.value, 2)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 5)
        self.assertEqual(s_list.len(), 5)

        #insert in tail of list
        s_list.insert(Node(5), Node(99))
        self.assertEqual(s_list.find(99).value, 99)
        self.assertEqual(s_list.find(99).next, None)
        self.assertEqual(s_list.find(99).prev.value, 5)
        self.assertEqual(s_list.find(1).prev, None)
        self.assertEqual(s_list.find(1).next.value, 2)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)
        s_list.len()
        self.assertEqual(s_list.len(), 6)

        #insert after head of list
        s_list.insert(Node(1), Node(11))
        self.assertEqual(s_list.find(11).value, 11)
        self.assertEqual(s_list.find(11).next.value, 2)
        self.assertEqual(s_list.find(11).prev.value, 1)
        self.assertEqual(s_list.find(1).prev, None)
        self.assertEqual(s_list.find(1).next.value, 11)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)
        self.assertEqual(s_list.len(), 7)

    def test_insert_with_None(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))

        #with non empty list
        s_list.insert(None, Node(99))
        self.assertEqual(s_list.find(99).value, 99)
        self.assertEqual(s_list.find(99).next, None)
        self.assertEqual(s_list.find(99).prev.value, 5)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 2)
        self.assertEqual(s_list.tail.prev.value, 5)
        self.assertEqual(s_list.tail.next, None)
        s_list.len()
        self.assertEqual(s_list.len(), 5)

        #with empty list
        s_list = LinkedList2()
        s_list.insert(None, Node(205))
        self.assertEqual(s_list.find(205).value, 205)
        self.assertEqual(s_list.head.value, 205)
        self.assertEqual(s_list.tail.value, 205)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)
        s_list.len()
        self.assertEqual(s_list.len(), 1)

    def test_insert_equal_number(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))

        s_list.insert(Node(1), Node(1))
        self.assertNotEqual(s_list.head, s_list.head.next)
        self.assertEqual(s_list.len(), 5)

        s_list.insert(Node(5), Node(5))
        self.assertNotEqual(s_list.tail, s_list.tail.prev)
        self.assertEqual(s_list.len(), 6)


class add_in_head(unittest.TestCase):
    def test_add_in_head(self):
        s_list = LinkedList2()

        #add in empty list
        s_list.add_in_head(Node(4))
        self.assertEqual(s_list.find(4).value, 4)
        self.assertEqual(s_list.head.value, 4)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)
        self.assertEqual(s_list.tail.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 1)

        #add in non empty list
        s_list.add_in_head(Node(88))
        self.assertEqual(s_list.find(88).value, 88)
        self.assertEqual(s_list.head.value, 88)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 4)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.tail.next, None)
        s_list.len()
        self.assertEqual(s_list.len(), 2)

        #add in non empty list
        s_list.add_in_head(Node(205))
        self.assertEqual(s_list.find(205).value, 205)
        self.assertEqual(s_list.head.value, 205)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.next.value, 88)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 3)

        #add in non empty list
        s_list.add_in_head(Node(35))
        self.assertEqual(s_list.find(35).value, 35)
        self.assertEqual(s_list.head.value, 35)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.next.value, 205)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)
        s_list.len()
        self.assertEqual(s_list.len(), 4)


class combine_all_methods(unittest.TestCase):
    def test_all_methods(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        s_list.insert(Node(11), Node(22))

        #check head and tail after inserting 
        self.assertEqual(s_list.head.value, 11)
        self.assertEqual(s_list.tail.value, 22)
        self.assertEqual(s_list.head.next.value, 22)
        self.assertEqual(s_list.tail.prev.value, 11)
        self.assertEqual(s_list.len(), 2)

        #add another element in tail
        s_list.add_in_tail(Node(48))
        self.assertEqual(s_list.head.next.value, 22)
        self.assertEqual(s_list.tail.value, 48)
        self.assertEqual(s_list.tail.prev.value, 22)
        self.assertEqual(s_list.len(), 3)

        #add another element in head with add_in_head
        s_list.add_in_head(Node(55))
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.head.next.value, 11)
        self.assertEqual(s_list.find(11).prev.value, 55)
        self.assertEqual(s_list.head.next.prev.value, 55)
        s_list.len()
        self.assertEqual(s_list.len(), 4)

        #add another element in head with add_in_head
        s_list.add_in_head(Node(99))
        self.assertEqual(s_list.head.value, 99)
        self.assertEqual(s_list.head.next.value, 55)
        self.assertEqual(s_list.find(55).prev.value, 99)
        self.assertEqual(s_list.head.next.prev.value, 99)
        self.assertEqual(s_list.len(), 5)

        #insert another element in tail (with afterNode = None)
        s_list.insert(None, Node(115))
        self.assertEqual(s_list.head.value, 99)
        self.assertEqual(s_list.tail.value, 115)
        self.assertEqual(s_list.tail.prev.value, 48)
        s_list.len()
        self.assertEqual(s_list.len(), 6)


class delete(unittest.TestCase):
    def test_delete_one_node(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))

        #delete node from head
        s_list.delete(1)
        self.assertEqual(s_list.head.value, 2)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 4)
        s_list.len()
        self.assertEqual(s_list.len(), 3)

        #delete node from tail
        s_list.delete(5)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.tail.prev.value, 2)
        self.assertEqual(s_list.len(), 2)

        #delete node from center
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))
        s_list.delete(2)
        
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.head.next.value, 4)
        self.assertEqual(s_list.head.next.prev.value, 1)
        s_list.len()
        self.assertEqual(s_list.len(), 3)

    def test_delete_all_nodes(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))

        #all nodes in list are equal
        s_list.delete(5, all=True)
        self.assertEqual(s_list.head, None)
        self.assertEqual(s_list.tail, None)
        self.assertEqual(s_list.len(), 0)
        
        #one node in list non equal (in head)
        s_list = LinkedList2()
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))

        s_list.delete(5, all=True)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 1)
        self.assertEqual(s_list.len(), 1)

        #one node in list non equal (in tail)
        s_list = LinkedList2()
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(1))

        s_list.delete(5, all=True)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 1)
        s_list.len()
        self.assertEqual(s_list.len(), 1)

class add_in_empty_list(unittest.TestCase):
    def test_add_and_insert_in_tail_for_empty_list(self):
        #add in tail
        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        #check head and tail
        self.assertEqual(s_list.head.value, 11)
        self.assertEqual(s_list.tail.value, 11)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)
        s_list.len()
        self.assertEqual(s_list.len(), 1)

        #insert in list
        s_list = LinkedList2()
        s_list.insert(None, Node(11))
        #check head and tail
        self.assertEqual(s_list.head.value, 11)
        self.assertEqual(s_list.tail.value, 11)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 1)

        #add in head
        s_list = LinkedList2()
        s_list.add_in_head(Node(11))
        #check head and tail
        self.assertEqual(s_list.head.value, 11)
        self.assertEqual(s_list.tail.value, 11)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)
        self.assertEqual(s_list.len(), 1)

if __name__ == '__main__':
    unittest.main()