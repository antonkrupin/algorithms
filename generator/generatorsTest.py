import unittest

from random import randint
from generators import infinityGenetator


class infinityGenetatorTest(unittest.TestCase):
    def test_shortList(self):
        values = [10, 100, 256]
        testResultList = []
        generatorResultList = []

        generatorResult = infinityGenetator(values)
        
        for i in range(len(values)):
            sumValues = 0
            for j in range(values[i]):
                sumValues += j
            testResultList.append(sumValues)
        
        for key in generatorResult[0]:
            generatorResultList.append(generatorResult[0][key])

        self.assertEqual(testResultList, generatorResultList)

    def test_randomList(self):
        values = []
        for i in range(100):
            elem = randint(1,100)
            values.append(elem)

        testResultList = []
        generatorResultList = []

        generatorResult = infinityGenetator(values)
        
        for i in range(len(values)):
            sumValues = 0
            for j in range(values[i]):
                sumValues += j
            testResultList.append(sumValues)
        
        for key in generatorResult[0]:
            generatorResultList.append(generatorResult[0][key])

        self.assertEqual(testResultList, generatorResultList)

    def test_longRandomList(self):
        values = []
        for i in range(100000):
            elem = randint(1,1000)
            values.append(elem)

        testResultList = []
        generatorResultList = []

        generatorResult = infinityGenetator(values)
        
        for i in range(len(values)):
            sumValues = 0
            for j in range(values[i]):
                sumValues += j
            testResultList.append(sumValues)
        
        for key in generatorResult[0]:
            generatorResultList.append(generatorResult[0][key])

        self.assertEqual(testResultList, generatorResultList)


if __name__ == '__main__':
    unittest.main()
