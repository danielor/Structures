import unittest
from Stack import Stack

class StackTest(unittest.TestCase):
    """
    A function that unit tests the Stack object 
    """
    def _build(self):
        """
        A function that builds a stack 
        """
        s = Stack()
        s.push('A')
        s.push('B')
        s.push('C')
        return s 

    def testIsEmpty(self):
        """
        Test Slack.isEmpty
        """
        s = Stack() 
        self.assertEqual(s.isEmpty(), True)
        s = self._build()
        self.assertEqual(s.isEmpty(), False)

    def testPush(self):
        """
        Test Stack.push 
        """
        s = self._build()
        self.assertEqual(str(s), '[A, B, C]')
        s.push('D')
        self.assertEqual(str(s), '[A, B, C, D]')

    def testPop(self):
        """
        Test Stack.pop 
        """
        s = self._build()
        self.assertEqual(str(s), '[A, B, C]')
        p = s.pop()
        self.assertEqual(p, 'C')
        self.assertEqual(str(s), '[A, B]')

    def testSize(self):
        """
        Test Stack.size 
        """
        s = self._build()
        self.assertEqual(s.size(), 3)
        p = s.pop()
        self.assertEqual(s.size(), 2)

    def testPeek(self):
        """
        Test Stack.peek
        """
        s = self._build()
        self.assertEqual(s.peek(), 'C')
        