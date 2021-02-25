import unittest

from stack import Stack

class stackPopTest(unittest.TestCase):
    def test_Push(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)
    
    def test_Size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.push(33)
        self.assertEqual(stack.size(), 3)
        stack.pop()
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)

    def test_Pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.size(), 4)
        stack.pop()
        self.assertEqual(stack.size(), 3)

    def test_Peek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        stack.push(5)
        stack.push(8)
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.size(), 2)
        stack.push(9)
        stack.pop()
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.size(), 1)



if __name__ == "__main__":
    unittest.main()