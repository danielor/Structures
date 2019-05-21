import unittest 
from Queue import Queue

class QueueTest(unittest.TestCase):
    """
    A function that unit tests the Queue 
    """
    def _build(self):
        """
        A function that builds a queue 
        """
        q = Queue()
        q.enqueue('A')
        return q

    def testIsEmpty(self):
        """
        Test Queue.isEmpty
        """
        q = Queue()
        self.assertEqual(q.isEmpty(), True)
        q = self._build()
        self.assertEqual(q.isEmpty(), False)

    def testEnqueue(self):
        """
        Test Queue.enqueue 
        """
        q = self._build()
        self.assertEqual(str(q), '[A]')
        q.enqueue('B')
        self.assertEqual(str(q), '[B, A]')

    def testDequeue(self):
        """
        Test Queue.dequeue
        """
        q = self._build()
        self.assertEqual(str(q), '[A]')
        q.enqueue('B')
        self.assertEqual(str(q), '[B, A]')
        q.dequeue()
        self.assertEqual(str(q), '[B]')

    def testSize(self):
        """
        Test Queue.size
        """
        q = self._build()
        self.assertEqual(q.size(), 1)
        q.enqueue('B')
        self.assertEqual(q.size(), 2)

    def testPeek(self):
        """
        Test Queue.peek 
        """
        q = self._build()
        q.enqueue('B')
        self.assertEqual(q.peek(), 'A')