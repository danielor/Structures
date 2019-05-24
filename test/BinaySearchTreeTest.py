import unittest 
from ds.tree.BinarySearchTree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
    """
    A collection of tests that test the Binary Search Tree 
    """
    def _build(self):
        """
        A function that builds the binary search tree
        """
        bst = BinarySearchTree(None)
        bst.insert(5)
        bst.insert(3)
        bst.insert(2)
        bst.insert(1)
        bst.insert(7)
        bst.insert(8)
        bst.insert(6)
        return bst 

    def testInsert(self):
        """
        Test BinarySearchTree.insert
        """
        bst = self._build()
        self.assertEqual(str(bst), '[1, 2, 3, 5, 6, 7, 8]')
        bst.insert(4)
        self.assertEqual(str(bst), '[1, 2, 3, 4, 5, 6, 7, 8]')

    def testSearch(self):
        """
        Test BinarySearchTree.search
        """
        bst = self._build()
        node = bst.search(1)
        self.assertEqual(node.data, 1)
        node = bst.search(12)
        self.assertEqual(node, None)

    def testMin(self):
        """
        Test BinarySearchTree.min 
        """
        bst = self._build()
        node = bst.min()
        self.assertEqual(node.data, 1)

    def testMax(self):
        """
        Test BinarySearchTree.max 
        """
        bst = self._build()
        node = bst.max()
        self.assertEqual(node.data, 8)

    def testTraverse(self):
        """
        Test BinarySearchTree.traverse
        """
        s = []
        bst = self._build()
        bst.traverse(s.append, traverse_type=BinarySearchTree.IN_ORDER)
        self.assertEqual(s, [1, 2, 3,  5, 6, 7, 8])
        s = []
        bst.traverse(s.append, traverse_type=BinarySearchTree.POST_ORDER)
        self.assertEqual(s, [1, 2, 3, 6, 7, 8, 5])
        s = []
        bst.traverse(s.append, traverse_type=BinarySearchTree.PRE_ORDER)
        self.assertEqual(s, [5, 1, 2, 3, 6, 7, 8])
