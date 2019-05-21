import unittest 
from DoublyLinkedList import DoublyLinkedList

class DoublyLinkedListTest(unittest.TestCase):
    """
    A function that unit tests the Doubly Linked List object 
    """
    def _build(self):
        """
        A function that builds a basic linked list 
        """
        ll = DoublyLinkedList(None)
        ll.prepend('A')
        return ll

    def testAppend(self):
        """
        Test DoublyLinkedListNode.append 
        """
        ll = self._build()
        ll.append('B')
        self.assertEqual(str(ll), '(A, B)')

    def testPrepend(self):
        """
        Test DoublyLinkedListNode.prepend
        """
        ll = self._build() 
        ll.prepend('B')
        self.assertEqual(str(ll), '(B, A)')

    def testFind(self):
        """
        Test DoublyLinkedListNode.find 
        """
        ll = self._build()
        self.assertEqual(str(ll.find('A')), '<DoublyLinkedListNode A>')
        self.assertEqual(ll.find('B') is None, True)
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll.find('B')), '<DoublyLinkedListNode B>')
        self.assertEqual(str(ll.find('C')), '<DoublyLinkedListNode C>')

    def testRemove(self):
        """
        Test DoublyLinkedListNode.remove 
        """
        ll = self._build()
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll), '(C, A, B)')
        ll.remove('A')
        self.assertEqual(str(ll), '(C, B)')

    def testReverse(self):
        """
        Test DoublyLinkedListNode.reverse
        """
        ll = self._build()
        ll.append('B')
        ll.prepend('C')
        self.assertEqual(str(ll), '(C, A, B)')
        ll.reverse()
        self.assertEqual(str(ll), '(B, A, C)')