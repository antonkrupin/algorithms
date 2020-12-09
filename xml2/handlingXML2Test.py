import unittest
import string
import random

from handlingXML2 import tagNodesList
from handlingXML2 import findParent
from handlingXML2 import deleteNodes


class tagNodesListTest(unittest.TestCase):
    def test_WithDifferentRootTags(self):
        self.assertEqual(tagNodesList('data','test1', 'demo.xml'), [['test1'],1])
        self.assertEqual(tagNodesList('test1','test1', 'demo.xml'), [[],-1])
        self.assertEqual(tagNodesList('wrongRootTag','test1', 'demo.xml'), [[],-1])

    def test_missedArgument(self):
        self.assertRaises(TypeError, tagNodesList)

    def test_WrongXMLFile(self):
        self.assertEqual(tagNodesList('data', 'test1', 'notExsistingXML.xml'), ['no file', -1])

class findParentTest(unittest.TestCase):
    def test_WithDifferentNodeTags(self):
        self.assertEqual(findParent('notExistingNode','demo.xml'), ['notExistingNode', -1])

    def test_WrongXMLFile(self):
        self.assertEqual(findParent('pc', 'notExsistingXML.xml'), ['no file', -1])

class deleteNodesTest(unittest.TestCase):
    def test_deletedNodes(self):
        deleteNodes('languages', 'demo.xml')
        test1 = tagNodesList('data', 'languages', 'fileWithDeletedNodes.xml')
        test2 = tagNodesList('data', 'languages', 'new_demo.xml')
        self.assertEqual(test1, test2)

    def test_WrongXMLFile(self):
        self.assertEqual(deleteNodes('pc','notExsisting.xml'), -1)

if __name__ == '__main__':
    unittest.main()