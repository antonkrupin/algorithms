import unittest
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
        
        psIntersection = ps.intersection([-5,9,1,11,131])
        self.assertEqual(len(psIntersection), 5)
        psIntersection = ps.intersection([-5])
        self.assertEqual(len(psIntersection), 1)
        psIntersection = ps.intersection([999,1000,111,22222])
        self.assertEqual(psIntersection, None)
        psIntersection = ps.intersection([])
        self.assertEqual(psIntersection, None)

    def test_powerSetIntersectionEmpty(self):
        ps = PowerSet()
        psIntersection = ps.intersection([-5,9,1,11,131])
        self.assertEqual(psIntersection, None)

        psIntersection = ps.intersection([])
        self.assertEqual(psIntersection, None)

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

        psUnion = ps.union([99,18,35])
        self.assertEqual(len(psUnion), 12)
        psUnion = ps.union([])
        self.assertEqual(len(psUnion), 10)

        ps = PowerSet()
        psUnion = ps.union([1, -5, 13, 0, 4, 9, 92, 131, 11, 18])
        self.assertEqual(len(psUnion), 10)

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

        psDiffirence = ps.difference([1, -5, 13, 0, 4, 9, 92, 131, 11, 18])
        self.assertEqual(psDiffirence, None)

        psDiffirence = ps.difference([1, -5, 13, 0, 4, 9, 92, 131, 11])
        self.assertEqual(len(psDiffirence), 1)

if __name__ == '__main__':
    unittest.main()
