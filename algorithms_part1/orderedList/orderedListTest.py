import unittest
from random import randint

from orderedList import Node, OrderedList, OrderedStringList

class orderedListAddTest(unittest.TestCase):
    def test_shortListAscendingTrue(self):
        ordList = OrderedList(True)
        self.assertEqual(ordList.head, None)
        self.assertEqual(ordList.tail, None)
        self.assertEqual(ordList.len(), 0)

        ordList.add(4)
        self.assertEqual(ordList.head.value, 4)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.len(), 1)

        ordList.add(-1)
        self.assertEqual(ordList.head.value, -1)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.len(), 2)

        ordList.add(0)
        self.assertEqual(ordList.head.value, -1)
        self.assertEqual(ordList.head.next.value, 0)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.len(), 3)

        ordList.add(10)
        self.assertEqual(ordList.head.value, -1)
        self.assertEqual(ordList.tail.value, 10)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 4)

    def test_shortListAscendingFalse(self):
        ordList = OrderedList(False)
        self.assertEqual(ordList.head, None)
        self.assertEqual(ordList.tail, None)
        self.assertEqual(ordList.len(), 0)

        ordList.add(-10)
        self.assertEqual(ordList.head.value, -10)
        self.assertEqual(ordList.tail.value, -10)
        self.assertEqual(ordList.len(), 1)

        ordList.add(20)
        self.assertEqual(ordList.head.value, 20)
        self.assertEqual(ordList.tail.value, -10)
        self.assertEqual(ordList.len(), 2)

        ordList.add(21)
        self.assertEqual(ordList.head.value, 21)
        self.assertEqual(ordList.head.next.value, 20)
        self.assertEqual(ordList.tail.value, -10)
        self.assertEqual(ordList.tail.prev.value, 20)
        self.assertEqual(ordList.len(), 3)

        ordList.add(-2)
        self.assertEqual(ordList.head.value, 21)
        self.assertEqual(ordList.head.next.value, 20)
        self.assertEqual(ordList.tail.value, -10)
        self.assertEqual(ordList.tail.prev.value, -2)
        self.assertEqual(ordList.len(), 4)

class orderedListFindTest(unittest.TestCase):
    def test_shortListFindAscendingTrue(self):
        ordList = OrderedList(True)
        ordList.add(0)
        ordList.add(10)
        ordList.add(4)
        ordList.add(-1)
        ordList.add(16)
        ordList.add(9)
        ordList.add(11)

        findEl = ordList.find(10)
        self.assertEqual(findEl.value, 10)

        findEl = ordList.find(16)
        self.assertEqual(findEl.value, 16)

        findEl = ordList.find(-222)
        self.assertEqual(findEl, None)

        findEl = ordList.find(9999)
        self.assertEqual(findEl, None)

    def test_shortListFindAscendingFalse(self):
        ordList = OrderedList(False)
        ordList.add(0)
        ordList.add(10)
        ordList.add(4)
        ordList.add(-1)
        ordList.add(16)
        ordList.add(9)
        ordList.add(11)

        findEl = ordList.find(10)
        self.assertEqual(findEl.value, 10)

        findEl = ordList.find(16)
        self.assertEqual(findEl.value, 16)

        findEl = ordList.find(-222)
        self.assertEqual(findEl, None)

        findEl = ordList.find(9999)
        self.assertEqual(findEl, None)

class orderedListDeleteTest(unittest.TestCase):
    def test_shortListDeleteAscendingTrue(self):
        ordList = OrderedList(True)
        ordList.add(0)
        ordList.add(10)
        ordList.add(4)
        ordList.add(-1)
        ordList.add(16)
        ordList.add(9)
        ordList.add(11)        

        delEl = ordList.delete(444)
        self.assertEqual(delEl, False)
        self.assertEqual(ordList.len(), 7)

        delEl = ordList.delete(-1)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 16)
        self.assertEqual(ordList.tail.prev.value, 11)
        self.assertEqual(ordList.len(), 6)

        delEl = ordList.delete(16)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 11)
        self.assertEqual(ordList.tail.prev.value, 10)
        self.assertEqual(ordList.len(), 5)

        delEl = ordList.delete(9)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 11)
        self.assertEqual(ordList.tail.prev.value, 10)
        self.assertEqual(ordList.len(), 4)

        delEl = ordList.delete(10)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 11)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 3)

        delEl = ordList.delete(11)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.tail.prev.value, 0)
        self.assertEqual(ordList.len(), 2)

        delEl = ordList.delete(4)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next, None)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev, None)
        self.assertEqual(ordList.len(), 1)

        delEl = ordList.delete(0)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head, None)
        self.assertEqual(ordList.tail, None)
        self.assertEqual(ordList.len(), 0)

    def test_shortListDeleteAscendingFalse(self):
        ordList = OrderedList(False)
        ordList.add(0)
        ordList.add(10)
        ordList.add(4)
        ordList.add(-1)
        ordList.add(16)
        ordList.add(9)
        ordList.add(11)        

        delEl = ordList.delete(444)
        self.assertEqual(delEl, False)
        self.assertEqual(ordList.len(), 7)

        delEl = ordList.delete(-1)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 16)
        self.assertEqual(ordList.head.next.value, 11)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 6)

        delEl = ordList.delete(16)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 11)
        self.assertEqual(ordList.head.next.value, 10)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 5)

        delEl = ordList.delete(9)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 11)
        self.assertEqual(ordList.head.next.value, 10)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 4)

        delEl = ordList.delete(10)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 11)
        self.assertEqual(ordList.head.next.value, 4)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 3)

        delEl = ordList.delete(11)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 4)
        self.assertEqual(ordList.head.next.value, 0)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev.value, 4)
        self.assertEqual(ordList.len(), 2)

        delEl = ordList.delete(4)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.head.next, None)
        self.assertEqual(ordList.tail.value, 0)
        self.assertEqual(ordList.tail.prev, None)
        self.assertEqual(ordList.len(), 1)

        delEl = ordList.delete(0)
        self.assertEqual(delEl, True)
        self.assertEqual(ordList.head, None)
        self.assertEqual(ordList.tail, None)
        self.assertEqual(ordList.len(), 0)

class orderedListCombineAddAndDeleteTest(unittest.TestCase):
    def test_shortListAddAndDeleteAscendingTrue(self):
        ordList = OrderedList(True)
        ordList.add(0)
        ordList.add(10)
        ordList.add(4)

        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.tail.value, 10)
        self.assertEqual(ordList.len(), 3)

        delEl = ordList.delete(10)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.len(), 2)

        ordList.add(11)
        ordList.add(15)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.tail.value, 15)
        self.assertEqual(ordList.len(), 4)

        delEl = ordList.delete(11)
        self.assertEqual(ordList.head.value, 0)
        self.assertEqual(ordList.tail.value, 15)
        self.assertEqual(ordList.len(), 3)

        ordList.add(-8)
        delEl = ordList.delete(15)
        self.assertEqual(ordList.head.value, -8)
        self.assertEqual(ordList.tail.value, 4)
        self.assertEqual(ordList.len(), 3)

if __name__ == '__main__':
    unittest.main()