import unittest
from random import randint
from checkSubString import checkSubString as check

class checkSubStringTests(unittest.TestCase):

    def testRegression(self):
        self.assertEqual(check('12345','234'),  True)
        self.assertEqual(check('12345','2346'),False)
        self.assertEqual(check('hello world', 'lo w'), True)
        self.assertEqual(check('hello world', 'low'), False)

    def testRandom(self):
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

        try:
            self.assertEqual(check('2345',''), False)
            self.assertTrue(False)
        except:
            pass

    def testMax(self):
        self.assertEqual(check(
            '12341234578998754554667788432333444456677888899900923211342546546546', 
            '7788432333444456677'), True)
        self.assertEqual(check(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
            'tempor incididunt'), True)

if __name__ == 'main':
    unittest.main()