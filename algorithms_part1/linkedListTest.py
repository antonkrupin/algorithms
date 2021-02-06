import unittest

from random import randint
from linkedList import Node, LinkedList


class add_in_tail(unittest.TestCase):
    def test_add_in_empty_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(5))
        self.assertEqual(s_list.len(), 1)

    def test_add_in_list(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))
        s_list_example.add_in_tail(Node(1))
        s_list_example.add_in_tail(Node(6))
        s_list_example.add_in_tail(Node(8))
        s_list_example.add_in_tail(Node(11))
        s_list_example.add_in_tail(Node(77))

        s_list = s_list_example
        s_list.add_in_tail(Node(88))
        self.assertEqual(s_list.len(), s_list_example.len())


class find(unittest.TestCase):
    def test_find_in_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.find(5))

    def test_find_in_list(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))
        s_list_example.add_in_tail(Node(1))
        s_list_example.add_in_tail(Node(6))
        s_list_example.add_in_tail(Node(8))
        s_list_example.add_in_tail(Node(11))
        s_list_example.add_in_tail(Node(77))

        self.assertIsNotNone(s_list_example.find(5))
        self.assertIsNotNone(s_list_example.find(77))
        self.assertIsNotNone(s_list_example.find(6))

    def test_find_in_short_random_list(self):
        s_list_example = LinkedList()
        listLength = randint(20,100)
        valuesForFind = []

        for i in range(1, listLength):
            value = randint(1,1000)
            s_list_example.add_in_tail(Node(value))
            valuesForFind.append(value)

        for i in range(10):
            index = randint(0,len(valuesForFind))
            value = valuesForFind[index]
            self.assertIsNotNone(s_list_example.find(value))

    def test_find_in_long_random_list(self):
        s_list_example = LinkedList()
        listLength = randint(10000,1000000)
        valuesForFind = []

        for i in range(1, listLength):
            value = randint(1,1000)
            s_list_example.add_in_tail(Node(value))
            valuesForFind.append(value)

        for i in range(100):
            index = randint(0,len(valuesForFind))
            value = valuesForFind[index]
            self.assertIsNotNone(s_list_example.find(value))


class find_all(unittest.TestCase):
    def test_find_in_empty_list(self):
        s_list_example = LinkedList()
        self.assertEqual(s_list_example.find_all(2), [])

    def test_find_in_list_with_one_node(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(34))

        self.assertEqual(s_list_example.find_all(Node(2)), [])
        self.assertEqual(len(s_list_example.find_all(34)), 1)

    def test_find_in_list_with_many_nodes(self):
        s_list_example = LinkedList()
        list_elements = [34, 45,1, 2,34, 6,8,12,34]
        for i in list_elements:
            s_list_example.add_in_tail(Node(i))

        self.assertEqual(s_list_example.find_all(Node(555)), [])
        self.assertEqual(len(s_list_example.find_all(34)), 3)
        self.assertEqual(len(s_list_example.find_all(45)), 1)


class delete(unittest.TestCase):
    def test_delete_from_short_list(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))
        s_list_example.add_in_tail(Node(1))
        s_list_example.add_in_tail(Node(6))
        s_list_example.add_in_tail(Node(8))
        s_list_example.add_in_tail(Node(11))
        s_list_example.add_in_tail(Node(77))

        s_list_example.delete(5)
        self.assertEqual(s_list_example.head.value,1)

    def test_delete_from_list_with_all_equal_nodes(self):
        s_list_example = LinkedList()
        for i in range(20):
            s_list_example.add_in_tail(Node(2))
        
        s_list_example.delete(2, all=True)
        self.assertEqual(s_list_example.len(), 0)
        self.assertEqual(s_list_example.head, None)
        self.assertEqual(s_list_example.tail, None)

    def test_delet_from_list_with_one_node(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(2))

        s_list_example.delete(2, all=True)

        self.assertEqual(s_list_example.len(), 0)
        self.assertEqual(s_list_example.head, None)
        self.assertEqual(s_list_example.tail, None)


class insert(unittest.TestCase):
    def test_insert_in_empty_list_with_none(self):
        s_list = LinkedList()
        s_list.insert(None,Node(2))
        self.assertEqual(s_list.len(),1)
        self.assertEqual(s_list.head, s_list.tail)

    def test_insert_in_list(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))
        s_list_example.add_in_tail(Node(1))
        s_list_example.add_in_tail(Node(6))
        s_list_example.add_in_tail(Node(8))
        s_list_example.add_in_tail(Node(11))
        s_list_example.add_in_tail(Node(77))

        s_list_example.insert(Node(5),Node(2))

        self.assertEqual(s_list_example.head.next.value, 2)
        
        s_list_example.insert(None, Node(8))

        self.assertEqual(s_list_example.head.value, 8)

        s_list_example.insert(Node(77), Node(99))

        self.assertEqual(s_list_example.tail.value, 99)

    def test_insert_in_list_with_one_node(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))

        s_list_example.insert(Node(5),Node(2))

        self.assertEqual(s_list_example.len(), 2)
        self.assertEqual(s_list_example.head.value,5)
        self.assertEqual(s_list_example.tail.value,2)
        self.assertNotEqual(s_list_example.head, s_list_example.tail)

        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))

        s_list_example.insert(None, Node(2))

        self.assertEqual(s_list_example.len(), 2)
        self.assertEqual(s_list_example.head.value,2)
        self.assertEqual(s_list_example.tail.value,5)
        self.assertNotEqual(s_list_example.head, s_list_example.tail)


if __name__ == '__main__':
    unittest.main()