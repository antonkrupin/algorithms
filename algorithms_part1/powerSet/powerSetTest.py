import unittest
import time
from random import randint

from powerSet import PowerSet


class powerSetRemoveTest(unittest.TestCase):
    def test_powerSetRemove(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        self.assertEqual(ps.size(), 5)
        ps.remove(-5)
        self.assertEqual(ps.size(), 4)
        ps.remove(-5)
        self.assertEqual(ps.size(), 4)
    
    def test_powerSetRemoveFromEmptySet(self):
        ps = PowerSet()
        ps.remove(11)
        self.assertEqual(ps.size(), 0)

class powerSetPutTest(unittest.TestCase):
    def test_powerSetPut(self):
        ps = PowerSet()
        ps.put(1)
        self.assertEqual(ps.size(), 1)
        ps.put(1)
        self.assertEqual(ps.size(), 1)

class powerSetPutAndRemoveTest(unittest.TestCase):
    def test_powerSetPutRemove(self):
        ps = PowerSet()
        ps.put(1)
        self.assertEqual(ps.size(), 1)
        ps.put(-11)
        self.assertEqual(ps.size(), 2)
        ps.remove(18)
        self.assertEqual(ps.size(), 2)
        ps.put(12)
        ps.put(-4)
        self.assertEqual(ps.size(), 4)
        ps.remove(12)
        self.assertEqual(ps.size(), 3)

class powerSetIntersectionTest(unittest.TestCase):
    def test_powerSetIntersection(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)

        ps1 = PowerSet()
        ps1.put(-5)
        ps1.put(9)
        ps1.put(1)
        ps1.put(11)
        ps1.put(131)
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 5)

        ps1 = PowerSet()
        ps1.put(-5)
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 1)

        ps1 = PowerSet()
        ps1.put(999)
        ps1.put(1000)
        ps1.put(111)
        ps1.put(22222)
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 0)

        ps1 = PowerSet()
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 0)
    
    def test_powerSetIntersectionEmpty(self):
        ps = PowerSet()
        ps1 = PowerSet()
        ps1.put(-5)
        ps1.put(9)
        ps1.put(1)
        ps1.put(11)
        ps1.put(131)
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 0)

        ps1 = PowerSet()
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 0)

    def test_powerSetIntersectionHundredsElements(self):
        ps = PowerSet()
        ps1 = PowerSet()

        for i in range(1, 101):
            ps.put(i)

        for i in range(50, 151):
            ps1.put(i)

        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 51)
    
    def test_powerSetIntersectionManyElements(self):
        ps = PowerSet()
        ps1 = PowerSet()
        for i in range(1, 10001):
            ps.put(i)

        for i in range(9900, 20001):
            ps1.put(i)

        start_time = time.time()
        psIntersection = ps.intersection(ps1)
        self.assertEqual(psIntersection.size(), 101)
        print('time to processing', time.time() - start_time)

class powerSetUnionTest(unittest.TestCase):
    def test_powerSetUnion(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)

        ps1 = PowerSet()
        ps1.put(99)
        ps1.put(18)
        ps1.put(35)
        psUnion = ps.union(ps1)
        self.assertEqual(psUnion.size(), 12)

        ps1 = PowerSet()
        psUnion = ps.union(ps1)
        self.assertEqual(psUnion.size(), 10)

        ps = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        ps1.put(18)
        psUnion = ps.union(ps1)
        self.assertEqual(psUnion.size(), 10)

class powerSetDifferenceTest(unittest.TestCase):
    def test_powerSetDiffirence(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)

        ps1 = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        ps1.put(18)
        psDiffirence = ps.difference(ps1)
        self.assertEqual(psDiffirence.size(), 0)

        ps1 = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        psDiffirence = ps.difference(ps1)
        self.assertEqual(psDiffirence.size(), 1)

    def test_powerSetDiffirenceHundredsElements(self):
        ps = PowerSet()
        ps1 = PowerSet()

        for i in range(1, 101):
            ps.put(i)

        for i in range(50, 151):
            ps1.put(i)

        psDiffirence = ps.difference(ps1)
        self.assertEqual(psDiffirence.size(), 49)
    
    def test_powerSetDifferenceManyElements(self):
        ps = PowerSet()
        for i in range(1, 10001):
            ps.put(i)

        ps1 = PowerSet()
        for i in range(9900, 20001):
            ps1.put(i)

        start_time = time.time()
        psDiffirence = ps.difference(ps1)
        self.assertEqual(psDiffirence.size(), 9899)
        print('time to processing', time.time() - start_time)

class powerSetIssubsetTest(unittest.TestCase):
    def test_powerSetIssubsetAll(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)

        ps1 = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        ps1.put(18)

        psIssubset = ps.issubset(ps1)
        self.assertEqual(psIssubset, True)

    def test_powerSetIssubsetNotAll(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)
        ps.put(28)
        ps.put(-11)
        ps.put(999)

        ps1 = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        ps1.put(18)

        psIssubset = ps.issubset(ps1)
        self.assertEqual(psIssubset, True)

    def test_powerSetIssubsetNotAll1(self):
        ps = PowerSet()
        ps.put(1)
        ps.put(-5)
        ps.put(13)
        ps.put(0)
        ps.put(4)
        ps.put(9)
        ps.put(92)
        ps.put(131)
        ps.put(11)
        ps.put(18)
        ps.put(28)
        ps.put(-11)
        ps.put(999)

        ps1 = PowerSet()
        ps1.put(1)
        ps1.put(-5)
        ps1.put(13)
        ps1.put(0)
        ps1.put(4)
        ps1.put(9)
        ps1.put(92)
        ps1.put(131)
        ps1.put(11)
        ps1.put(18)
        ps1.put(55)
        ps1.put(888)

        psIssubset = ps.issubset(ps1)
        self.assertEqual(psIssubset, False)


if __name__ == '__main__':
    unittest.main()