import unittest
from random import randint

from queue import Queue


class queueEnqueueTest(unittest.TestCase):
    def test_enqueueInEmptyQueue(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(11)
        self.assertEqual(queue.size(), 2)
        queue.enqueue(44)
        self.assertEqual(queue.size(), 3)

    def test_enqueueWithRandom(self):
        queue = Queue()
        queueLen = randint(10, 1000)
        for i in range(queueLen):
            el = randint(5,100)
            queue.enqueue(el)
        self.assertEqual(queue.size(), queueLen)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(11)
        queue.enqueue(15)
        queue.enqueue(0)
        queue.enqueue(88)
        el = queue.dequeue()
        self.assertEqual(queue.size(), 4)
        self.assertEqual(el, 5)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 3)
        self.assertEqual(el, 11)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 2)
        self.assertEqual(el, 15)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 1)
        self.assertEqual(el, 0)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(el, 88)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(el, None)
    
    def test_dequeueRandom(self):
        queue = Queue()
        queueLen = randint(10, 1000)

        for i in range(queueLen):
            el = randint(5,100)
            queue.enqueue(el)

        for i in range(1, queueLen + 1):
            queue.dequeue()
            self.assertEqual(queue.size(), queueLen - i)
    
    def test_enqueueAndDequeue(self):
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(11)
        queue.enqueue(15)
        queue.enqueue(0)
        queue.enqueue(88)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 4)
        self.assertEqual(el, 5)

        queue.enqueue(99)
        self.assertEqual(queue.size(), 5)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 4)
        self.assertEqual(el, 11)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 3)
        self.assertEqual(el, 15)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 2)
        self.assertEqual(el, 0)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 1)
        self.assertEqual(el, 88)

        el = queue.dequeue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(el, 99)

        el = queue.dequeue()
        self.assertEqual(el, None)

        queue.enqueue(100)
        self.assertEqual(queue.size(), 1)
        el = queue.dequeue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(el, 100)


if __name__ == '__main__':
    unittest.main()