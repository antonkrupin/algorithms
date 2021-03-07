import unittest
from random import randint

from deque import Deque


class dequeueTest(unittest.TestCase):
    def test_addFront(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)
        deque.addFront(11)
        self.assertEqual(deque.size(), 1)
        deque.addFront(15)
        self.assertEqual(deque.size(), 2)

    def test_addTail(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)
        deque.addTail(11)
        self.assertEqual(deque.size(), 1)
        deque.addTail(15)
        self.assertEqual(deque.size(), 2)

    def test_removeFront(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)
        deque.addFront(11)
        self.assertEqual(deque.size(), 1)
        deque.addFront(15)
        self.assertEqual(deque.size(), 2)
        deque.addFront(54)
        deque.addFront(48)
        self.assertEqual(deque.size(), 4)

        removedEl = deque.removeFront()
        self.assertEqual(removedEl, 48)
        self.assertEqual(deque.size(), 3)

        removeEl = deque.removeFront()
        self.assertEqual(removeEl, 54)
        self.assertEqual(deque.size(), 2)

        removeEl = deque.removeFront()
        self.assertEqual(removeEl, 15)
        self.assertEqual(deque.size(), 1)

        removeEl = deque.removeFront()
        self.assertEqual(removeEl, 11)
        self.assertEqual(deque.size(), 0)

        removeEl = deque.removeFront()
        self.assertEqual(removeEl, None)
        self.assertEqual(deque.size(), 0)

    def test_removeTail(self):
        deque = Deque()
        self.assertEqual(deque.size(), 0)
        deque.addFront(11)
        self.assertEqual(deque.size(), 1)
        deque.addFront(15)
        self.assertEqual(deque.size(), 2)
        deque.addFront(54)
        deque.addFront(48)

        removedEl = deque.removeTail()
        self.assertEqual(removedEl, 11)
        self.assertEqual(deque.size(), 3)

        removedEl = deque.removeTail()
        self.assertEqual(removedEl, 15)
        self.assertEqual(deque.size(), 2)

        removedEl = deque.removeTail()
        self.assertEqual(removedEl, 54)
        self.assertEqual(deque.size(), 1)

        removedEl = deque.removeTail()
        self.assertEqual(removedEl, 48)
        self.assertEqual(deque.size(), 0)

        removedEl = deque.removeTail()
        self.assertEqual(removedEl, None)
        self.assertEqual(deque.size(), 0)

    def test_complex(self):
        deque = Deque()
        removeEl = deque.removeFront()
        self.assertEqual(removeEl, None)
        self.assertEqual(deque.size(), 0)

        removeEl = deque.removeTail()
        self.assertEqual(removeEl, None)
        self.assertEqual(deque.size(), 0)

        deque.addFront(11)
        self.assertEqual(deque.size(), 1)
        removeEl = deque.removeFront()
        self.assertEqual(removeEl, 11)
        self.assertEqual(deque.size(), 0)

        deque.addTail(15)
        removeEl = deque.removeTail()
        self.assertEqual(removeEl, 15)
        self.assertEqual(deque.size(), 0)

        deque.addFront(99)
        deque.addTail(15)
        deque.addFront(0)
        deque.addFront(44)
        deque.addTail(18)
        self.assertEqual(deque.size(), 5)

        removeEl = deque.removeFront()
        self.assertEqual(removeEl, 44)
        self.assertEqual(deque.size(), 4)

        removeEl = deque.removeTail()
        self.assertEqual(removeEl, 18)
        self.assertEqual(deque.size(), 3)

        deque.addTail(99)
        self.assertEqual(deque.size(), 4)

        removeEl = deque.removeTail()
        self.assertEqual(removeEl, 99)
        self.assertEqual(deque.size(), 3)


if __name__ == "__main__":
    unittest.main()