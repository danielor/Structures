import unittest
from test.LinkedListTest import LinkedListTest

def runAllTests():
    """
    The main entry point to run all of the unit tests 
    """
    structureSuite = unittest.TestSuite()
    structureSuite.addTest(unittest.makeSuite(LinkedListTest))
    runner = unittest.TextTestRunner()
    runner.run(structureSuite)

if __name__ == '__main__':
    runAllTests()