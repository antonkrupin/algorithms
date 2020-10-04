import unittest
import string
import random
from random import randint
from checkSubString import checkSubString as check

class checkSubStringTests(unittest.TestCase):

    def testRegression(self):
        self.assertEqual(check('12345','234'),  True)
        self.assertEqual(check('12345','2346'),False)
        self.assertEqual(check('hello world', 'lo w'), True)
        self.assertEqual(check('hello world', 'low'), False)

    def testRandom(self):
        for x in range(10000):
            string1 = []
            string2 = []

            for x in range(1,10):
                string1.append(randint(1,10))

            string1 = ''.join(map(str,string1))

            for x in range(4):
                string2.append(randint(1,10))

            string2 = ''.join(map(str,string2))

            checkRandom = check(string1,string2)
            self.assertEqual(checkRandom,string2 in string1)

    def testNull(self):
        self.assertEqual(check('2345','23'),True)
        self.assertEqual(check('','23'),False)
        self.assertEqual(check('',''), False)

        try:
            self.assertEqual(check('2345',''), False)
            self.assertTrue(False)
        except:
            pass
        
        try:
            self.assertEqual(check('',''), False)
            self.assertTrue(False)
        except:
            pass

        try:
            self.assertEqual(check('','234'), False)
            self.assertEqual(False)
        except:
            pass

    def testMax(self):

        def generateString(size):
            return ''.join(random.choice(string.ascii_letters) for _ in range(size))

        string1 = generateString(1000000)
        string2 = generateString(1000)

        checkRandom = check(string1,string2)
        self.assertEqual(checkRandom,string2 in string1)
        
if __name__ == 'main':
    unittest.main()