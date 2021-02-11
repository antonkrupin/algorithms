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

        #add in non empty list
        s_list.add_in_tail(Node(8))
        self.assertEqual(s_list.find(8).value, 8)
        self.assertEqual(s_list.head.value, 4)
        self.assertEqual(s_list.tail.value, 8)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 8)
        self.assertEqual(s_list.tail.prev.value, 4)
        self.assertEqual(s_list.tail.next, None)

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

        #insert in tail of list
        s_list.insert(Node(5), Node(99))
        self.assertEqual(s_list.find(99).value, 99)
        self.assertEqual(s_list.find(99).next, None)
        self.assertEqual(s_list.find(99).prev.value, 5)
        self.assertEqual(s_list.find(1).prev, None)
        self.assertEqual(s_list.find(1).next.value, 2)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)

        #insert after head of list
        s_list.insert(Node(1), Node(11))
        self.assertEqual(s_list.find(11).value, 11)
        self.assertEqual(s_list.find(11).next.value, 2)
        self.assertEqual(s_list.find(11).prev.value, 1)
        self.assertEqual(s_list.find(1).prev, None)
        self.assertEqual(s_list.find(1).next.value, 11)
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 99)

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

        #with empty list
        s_list = LinkedList2()
        s_list.insert(None, Node(205))
        self.assertEqual(s_list.find(205).value, 205)
        self.assertEqual(s_list.head.value, 205)
        self.assertEqual(s_list.tail.value, 205)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next, None)

    
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

        #add in non empty list
        s_list.add_in_head(Node(88))
        self.assertEqual(s_list.find(88).value, 88)
        self.assertEqual(s_list.head.value, 88)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.head.next.value, 4)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.tail.next, None)

        #add in non empty list
        s_list.add_in_head(Node(205))
        self.assertEqual(s_list.find(205).value, 205)
        self.assertEqual(s_list.head.value, 205)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.next.value, 88)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)

        #add in non empty list
        s_list.add_in_head(Node(35))
        self.assertEqual(s_list.find(35).value, 35)
        self.assertEqual(s_list.head.value, 35)
        self.assertEqual(s_list.tail.value, 4)
        self.assertEqual(s_list.head.next.value, 205)
        self.assertEqual(s_list.tail.prev.value, 88)
        self.assertEqual(s_list.head.prev, None)
        self.assertEqual(s_list.tail.next, None)

if __name__ == '__main__':
    unittest.main()