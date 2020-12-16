import unittest
from random import randint

from concurrency import sumWIthDividingIntoProcesses

class sumWIthDividingIntoProcessesTest(unittest.TestCase):
    def test_shortList(self):
        elementsForSum = [1,2,3,4,5,6,7,8,9,10]
        cycleForSum = 0

        for i in elementsForSum:
            cycleForSum += i

        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 10)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 1)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 3)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 7)[0], cycleForSum)

    def test_shortRandomList(self):
        elementsForSum = []
        cycleForSum = 0

        for i in range(1,11):
            elem = randint(1,10)
            elementsForSum.append(elem)

        for i in elementsForSum:
            cycleForSum += i

        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 10)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 1)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 3)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 7)[0], cycleForSum)

    def test_longRandomList(self):
        elementsForSum = []
        cycleForSum = 0

        for i in range(1,1001):
            elem = randint(1,10)
            elementsForSum.append(elem)

        for i in elementsForSum:
            cycleForSum += i

        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 10)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 1)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 3)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 7)[0], cycleForSum)
    
    def test_reallyLongRandomList(self):
        elementsForSum = []
        cycleForSum = 0

        for i in range(1,1000000):
            elem = randint(1,1000)
            elementsForSum.append(elem)

        for i in elementsForSum:
            cycleForSum += i

        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 100)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 500)[0], cycleForSum)
        self.assertEqual(sumWIthDividingIntoProcesses(elementsForSum, 200)[0], cycleForSum)

if __name__ == '__main__':
    unittest.main()