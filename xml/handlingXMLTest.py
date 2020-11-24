import unittest
import string
import random
from handlingXML import tagValues
from handlingXML import documentNodesWithAttribute as documentNodes


class tagValuesTest(unittest.TestCase):
    def test_regression(self):
        self.assertEqual(tagValues('notExsistingTag','demo.xml'), ['notExsistingTag',1])
        self.assertEqual(tagValues('sex','demo.xml'), ['sex', 1])

    def test_missedArgument(self):
        self.assertRaises(TypeError, tagValues)

    def test_randomTag(self):
        tag = []
        for i in range(100):
            i = random.choice(string.ascii_letters)
            tag.append(i)
        tag = ''.join(tag)
        result = tagValues(tag, 'demo.xml')
        self.assertEqual(result, tagValues(tag, 'demo.xml'))

    def test_randomLongTag(self):
        tag = []
        for i in range(1000000):
            i = random.choice(string.ascii_letters)
            tag.append(i)
        tag = ''.join(tag)
        result = tagValues(tag, 'demo.xml')
        self.assertEqual(result, tagValues(tag, 'demo.xml'))

    def test_longTag(self):
        self.assertEqual(tagValues('dsafjaewreoiureituruiyfdsgfdhewriuewytieruyireutyreiutyreutyeriutyreuityreityreuiterhgjdfhgjdgduyguyerteyeruityreuityreityeriut', 'demo.xml'),
                                    ['dsafjaewreoiureituruiyfdsgfdhewriuewytieruyireutyreiutyreutyeriutyreuityreityreuiterhgjdfhgjdgduyguyerteyeruityreuityreityeriut', 1])


class documentNodesTest(unittest.TestCase):
    def test_regression(self):
        self.assertEqual(documentNodes('notExsistingAttribute','demo.xml'), [0,1])
        self.assertEqual(documentNodes('name','demo.xml'), [7,1])

    def test_missedArgument(self):
        self.assertRaises(TypeError, documentNodes)

    def test_randomAttribute(self):
        tag = []
        for i in range(100):
            i = random.choice(string.ascii_letters)
            tag.append(i)
        tag = ''.join(tag)
        result = tagValues(tag, 'demo.xml')
        self.assertEqual(result, tagValues(tag, 'demo.xml'))

    def test_randomLongAttribute(self):
        tag = []
        for i in range(1000000):
            i = random.choice(string.ascii_letters)
            tag.append(i)
        tag = ''.join(tag)
        result = tagValues(tag, 'demo.xml')
        self.assertEqual(result, tagValues(tag, 'demo.xml'))

    def test_longAttribute(self):
        self.assertEqual(documentNodes('erweiuryewuiryishfjksdhfsjkhfsdfruiweyruiewyrewirewhfsdjkhfsdkfhdsjkhrfweiyrwieuyteiwtyeritweoruweoruweoruowetureotyret', 'demo.xml'), [1,1])

if __name__ == '__main__':
    unittest.main()