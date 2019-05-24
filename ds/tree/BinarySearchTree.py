from ds.node.BinaryTreeNode import BinaryTreeNode

class BinarySearchTree(object):
    """
    An implementation of the binary search tree 
    """
    IN_ORDER = 0 
    PRE_ORDER = 1
    POST_ORDER = 2
    def __init__(self, root):
        """
        The constructor of the binary search tree 
        :param root The root node
        """
        self.root = root

    def __str__(self):
        """
        A function that returns a string representation of the tree
        """
        s = []        
        self.traverse(s.append)
        return '[' + ', '.join([str(l) for l in s]) + ']'

    def search(self, val):
        """
        A function that searches the binary search tree 
        :param val The value to search
        """
        return self._search(self.root, val)

    def _search(self, node, val):
        """
        A function that searches from the root 
        :param node The current node
        :param val The value to search
        """
        if not node:
            return None 
        
        if node.data == val:
            return node

        if(val < node.data):
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
    
    def min(self):
        """
        A function that finds the minimum value in the tree 
        """
        current = self.root
        while current.left != None: 
            current = current.left 
        return current

    def max(self):
        """
        A function that finds the maximum value in the tree
        """
        current = self.root
        while current.right != None: 
            current = current.right 
        return current        

    def traverse(self, f, traverse_type = None):
        """ 
        A function that traverses the binary search tree and calls f
        :param f The function 
        :param traverse_type The type of traversal
        """
        return self._traverse(self.root, f, traverse_type=traverse_type)

    def _traverse(self, node, f, traverse_type = None):
        """
        A function that traverse the nodes an in order traversal 
        :param node The current node
        :param f The function 
        :param traverse_type The traversal type
        """
        if node: 
            if traverse_type == BinarySearchTree.PRE_ORDER:
                f(node.data)
            self._traverse(node.left, f)
            if not traverse_type:
                f(node.data)
            self._traverse(node.right, f)
            if traverse_type == BinarySearchTree.POST_ORDER:
                f(node.data)

    def insert(self,data):
        """
        A function that inserts the data into the binary search tree 
        :param data The data 
        """
        if not self.root:
            self.root = BinaryTreeNode(data, None, None, None)
            return 

        return self._insert(data, self.root)

    def _insert(self, data, node):
        """
        A function that inserts the node from data 
        :param data The data 
        :param node The current node 
        """
        less = data < node.data
        if less: 
            if node.left:
                return self._insert(data, node.left) 
        else:
            if node.right:
                return self._insert(data, node.right)
        new_node = BinaryTreeNode(data, node, None, None)
        if less:
            node.left = new_node
        else:
            node.right = new_node
        
   