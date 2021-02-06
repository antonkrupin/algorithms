import unittest

from random import randint
from linkedList import LinkedList, Node
from linkedListMerge import mergeLists


class mergeListsTest(unittest.TestCase):
    def test_mergeEmptyLists(self):
        list1 = LinkedList()
        list2 = LinkedList()

        self.assertEqual(mergeLists(list1, list2), [[], 1])

    def test_mergeListsWithEqualLength(self):
        list1 = LinkedList()
        list2 = LinkedList()

        elements1 = [2,3,4,5,6]
        elements2 = [5,1,2,8,11]
        testElementsSum = []

        for i in range(len(elements1)):
            testElementsSum.append(elements1[i] + elements2[i])

        for i in elements1:
            list1.add_in_tail(Node(i))

        for i in elements2:
            list2.add_in_tail(Node(i))

        self.assertEqual(mergeLists(list1, list2)[0], testElementsSum)

    def test_mergeListsWithNonEqualLength(self):
        list1 = LinkedList()
        list2 = LinkedList()

        elements1 = [2,3,4,5,6,7]
        elements2 = [5,1,2,8,11]
        
        for i in elements1:
            list1.add_in_tail(Node(i))

        for i in elements2:
            list2.add_in_tail(Node(i))

        self.assertEqual(mergeLists(list1, list2), [[], -1])

if __name__ == "__main__":
    unittest.main()