import unittest
from test.LinkedListTest import LinkedListTest
from test.DoublyLinkedListTest import DoublyLinkedListTest

def runAllTests():
    """
    The main entry point to run all of the unit tests 
    """
    structureSuite = unittest.TestSuite()
    structureSuite.addTest(unittest.makeSuite(LinkedListTest))
    structureSuite.addTest(unittest.makeSuite(DoublyLinkedListTest))
    runner = unittest.TextTestRunner()
    runner.run(structureSuite)

if __name__ == '__main__':
    runAllTests()