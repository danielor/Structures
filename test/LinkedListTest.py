import unittest
from ds.linear.LinkedList import LinkedList

class LinkedListTest(unittest.TestCase):
    """
    A function that unit tests the Linked List object
    """
    def _build(self):
        """
        A function that builds a basic linked list 
        """
        ll = LinkedList(None)
        ll.prepend('A')
        return ll

    def testAppend(self):
        """
        Test LinkedListNode.append 
        """
        ll = self._build()
        ll.append('B')
        self.assertEqual(str(ll), '(A, B)')

    def testPrepend(self):
        """
        Test LinkedListNode.prepend
        """
        ll = self._build() 
        ll.prepend('B')
        self.assertEqual(str(ll), '(B, A)')

    def testFind(self):
        """
        Test LinkedListNode.find 
        """
        ll = self._build()
        self.assertEqual(str(ll.find('A')), '<LinkListNode A>')
        self.assertEqual(ll.find('B') is None, True)
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll.find('B')), '<LinkListNode B>')
        self.assertEqual(str(ll.find('C')), '<LinkListNode C>')

    def testRemove(self):
        """
        Test LinkedListNode.remove 
        """
        ll = self._build()
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll), '(C, A, B)')
        ll.remove('A')
        self.assertEqual(str(ll), '(C, B)')

    def testReverse(self):
        """
        Test LinkedListNode.reverse
        """
        ll = self._build()
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll), '(C, A, B)')
        ll.reverse()
        self.assertEqual(str(ll), '(B, A, C)')


