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


class delete(unittest.TestCase):
    def test_delete_from_short_list(self):
        s_list_example = LinkedList()
        s_list_example.add_in_tail(Node(5))
        s_list_example.add_in_tail(Node(1))
        s_list_example.add_in_tail(Node(6))
        s_list_example.add_in_tail(Node(8))
        s_list_example.add_in_tail(Node(11))
        s_list_example.add_in_tail(Node(77))

        

if __name__ == '__main__':
    unittest.main()