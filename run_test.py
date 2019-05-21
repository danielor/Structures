import unittest
from test.DoublyLinkedListTest import DoublyLinkedListTest
from test.LinkedListTest import LinkedListTest
from test.QueueTest import QueueTest
from test.StackTest import StackTest

def runAllTests():
    """
    The main entry point to run all of the unit tests 
    """
    structureSuite = unittest.TestSuite()
    structureSuite.addTest(unittest.makeSuite(LinkedListTest))
    structureSuite.addTest(unittest.makeSuite(DoublyLinkedListTest))
    structureSuite.addTest(unittest.makeSuite(QueueTest))
    structureSuite.addTest(unittest.makeSuite(StackTest))
    runner = unittest.TextTestRunner()
    runner.run(structureSuite)

if __name__ == '__main__':
    runAllTests()