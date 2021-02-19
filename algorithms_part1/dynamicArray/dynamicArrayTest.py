import unittest

from random import randint
from dynamicArray import DynArray


class resizeDynamicArrayTest(unittest.TestCase):
    def test_resizeEmptyArray(self):
        test_da = DynArray()
        self.assertEqual(test_da.capacity, 16)
        test_da.resize(48)
        self.assertEqual(test_da.capacity, 48)

    def test_resizeNonEmptyArray(self):
        test_da = DynArray()

        for i in range(12):
            test_da.append(i)

        self.assertEqual(test_da.capacity, 16)
        test_da.resize(48)
        self.assertEqual(test_da.capacity, 48)

class insertInDynamicArrayTest(unittest.TestCase):
    def test_insertInEmpyArray(self):
        test_da = DynArray()
        test_da.insert(0, 50)

        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da.capacity, 16)
        
        test_da.insert(1, 99)
        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da[1], 99)
        self.assertEqual(test_da.capacity, 16)

        test_da.insert(0, 101)
        self.assertEqual(test_da[0], 101)
        self.assertEqual(test_da[1], 50)
        self.assertEqual(test_da[2], 99)
        self.assertEqual(test_da.capacity, 16)

    def test_insertInNonEmptyArray(self):
        test_da = DynArray()

        for i in range(10):
            test_da.append(i)

        self.assertEqual(test_da.capacity, 16)

        test_da.insert(0, 50)
        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da.capacity, 16)

        test_da.insert(11, 66)
        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da[11], 66)
        self.assertEqual(test_da.capacity, 16)

        test_da.insert(2, 99)
        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da[2], 99)
        self.assertEqual(test_da[12], 66)
        self.assertEqual(test_da.capacity, 16)

    
    def test_insertWithWrongIndex(self):
        test_da = DynArray()
        
        #in empyt array
        with self.assertRaises(IndexError):
            test_da.insert(-1, 50)

        test_da = DynArray()
        for i in range(15):
            test_da.append(i)

        #in non empty array
        with self.assertRaises(IndexError):
            test_da.insert(99, 11)

    #test when array len == capacity
    def test_insertWithResize(self):
        test_da = DynArray()
        for i in range(16):
            test_da.append(i)
        
        self.assertEqual(test_da.capacity, 16)
        test_da.insert(0, 50)
        self.assertEqual(test_da[0], 50)
        self.assertEqual(test_da[16], 15)
        self.assertEqual(test_da.capacity, 32)


class deleteFromDynamicArrayTest(unittest.TestCase):
    def test_deleteFromEmptyArray(self):
        test_da = DynArray()

        with self.assertRaises(IndexError):
            test_da.delete(2)

        with self.assertRaises(IndexError):
            test_da.delete(-1)

        with self.assertRaises(IndexError):
            test_da.delete(99)

        for i in range(10):
            test_da.append(i)

        with self.assertRaises(IndexError):
            test_da.delete(-1)

        with self.assertRaises(IndexError):
            test_da.delete(99)


    def test_deleteFromNonEmptyArray(self):
        test_da = DynArray()

        for i in range(10):
            test_da.append(i)

        test_da.delete(0)
        self.assertEqual(test_da[0], 1)
        self.assertEqual(test_da[1], 2)
        self.assertEqual(test_da[8], 9)
        self.assertEqual(test_da.capacity, 16)

        test_da.delete(8)
        self.assertEqual(test_da[0], 1)
        self.assertEqual(test_da[1], 2)
        self.assertEqual(test_da[7], 8)
        self.assertEqual(test_da.capacity, 16)

        with self.assertRaises(IndexError):
            test_da.delete(-1)

        with self.assertRaises(IndexError):
            test_da.delete(100)

    def test_deleteFromNonEmptyArrayWithResize(self):
        test_da = DynArray()

        for i in range(49):
            test_da.append(i)

        self.assertEqual(test_da.capacity, 64) 

        for i in range(19):
            test_da.delete(i)

        self.assertEqual(test_da.capacity, 42)
        
if __name__ == "__main__":
    unittest.main()