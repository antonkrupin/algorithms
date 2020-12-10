import unittest

from random import randint
from iterator import ListWithConstructor
from iterator import ListWithConstructorInfinite


class ListWithConstructorTest(unittest.TestCase):
    def test_littleQuantityOfElements(self):
        exampleSequence = [10,20,40,80,160,320,640,1280,2560]
        resultSequence = []

        for i in ListWithConstructor(10):
            resultSequence.append(i)
        
        self.assertEqual(exampleSequence, resultSequence)

    def test_randomElementsQuantity(self):
        randomNumber = randint(10,100)
        exampleSequence = []
        resultSequence = []
        
        number = randomNumber
        for i in range(1,10):
            exampleSequence.append(number)
            number = number*2

        for i in ListWithConstructor(randomNumber):
            resultSequence.append(i)

        self.assertEqual(exampleSequence, resultSequence)

    def test_randomElementsBigQuantity(self):
        randomNumber = randint(10000, 1000000)
        exampleSequence = []
        resultSequence = []

        number = randomNumber
        for i in range(1, 10):
            exampleSequence.append(number)
            number = number * 2
        
        for i in ListWithConstructor(randomNumber):
            resultSequence.append(i)

        self.assertEqual(exampleSequence, resultSequence)

    def test_cycleRandomElementsBigQuantity(self):
        for i in range(1,5):
            randomNumber = randint(10000, 1000000)
            exampleSequence = []
            resultSequence = []
            number = randomNumber
            for i in range(1, 10):
                exampleSequence.append(number)
                number = number * 2
        
            for i in ListWithConstructor(randomNumber):
                resultSequence.append(i)

            self.assertEqual(exampleSequence, resultSequence)


class ListWithConstructorInfiniteTest(unittest.TestCase):
    def test_littleQuantityOfElements(self):
        exampleSequence = [1,2,3,4,5,6,7,8,9,10]
        resultSequence = []

        for i in ListWithConstructorInfinite(10, False):
            resultSequence.append(i)
        
        self.assertEqual(exampleSequence, resultSequence)

    def test_randomElementsQuantity(self):
        randomNumber = randint(10,100)
        exampleSequence = []
        resultSequence = []

        for i in range(1,randomNumber+1):
            exampleSequence.append(i)

        for i in ListWithConstructorInfinite(randomNumber, False):
            resultSequence.append(i)

        self.assertEqual(exampleSequence, resultSequence)

    def test_randomElementsBigQuantity(self):
        randomNumber = randint(10000, 1000000)
        exampleSequence = []
        resultSequence = []

        for i in range(1, randomNumber+1):
            exampleSequence.append(i)
        
        for i in ListWithConstructorInfinite(randomNumber, False):
            resultSequence.append(i)

        self.assertEqual(exampleSequence, resultSequence)

    def test_cycleRandomElementsBigQuantity(self):
        for i in range(1,5):
            randomNumber = randint(10000, 1000000)
            exampleSequence = []
            resultSequence = []
            for i in range(1, randomNumber+1):
                exampleSequence.append(i)
        
            for i in ListWithConstructorInfinite(randomNumber, False):
                resultSequence.append(i)

            self.assertEqual(exampleSequence, resultSequence)

if __name__ == '__main__':
    unittest.main()