import os
import unittest
import string
import random

from handlingXML2 import tagNodesList
from handlingXML2 import findParent
from handlingXML2 import deleteNodes


STARTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'demo.xml')
RESULTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'new_demo.xml')
EXAMPLEDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'fileWithDeletedNodes.xml')
NOTEXSISTINGDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'notExsistingXML.xml')

class tagNodesListTest(unittest.TestCase):
    def test_WithDifferentRootTags(self):
        self.assertEqual(tagNodesList('data','test1', STARTDATA_FILENAME), [['test1'],1])
        self.assertEqual(tagNodesList('test1','test1', STARTDATA_FILENAME), [[],-1])
        self.assertEqual(tagNodesList('wrongRootTag','test1', STARTDATA_FILENAME), [[],-1])

    def test_missedArgument(self):
        self.assertRaises(TypeError, tagNodesList)

    def test_WrongXMLFile(self):
        self.assertEqual(tagNodesList('data', 'test1', NOTEXSISTINGDATA_FILENAME), ['no file', -1])

class findParentTest(unittest.TestCase):
    def test_WithDifferentNodeTags(self):
        self.assertEqual(findParent('notExistingNode', STARTDATA_FILENAME), ['notExistingNode', -1])

    def test_WrongXMLFile(self):
        self.assertEqual(findParent('pc', NOTEXSISTINGDATA_FILENAME), ['no file', -1])

class deleteNodesTest(unittest.TestCase):
    def test_deletedNodes(self):
        deleteNodes('languages', STARTDATA_FILENAME)
        test1 = tagNodesList('data', 'languages', EXAMPLEDATA_FILENAME)
        test2 = tagNodesList('data', 'languages', RESULTDATA_FILENAME)
        self.assertEqual(test1, test2)

    def test_WrongXMLFile(self):
        self.assertEqual(deleteNodes('pc', NOTEXSISTINGDATA_FILENAME), -1)

if __name__ == '__main__':
    unittest.main()