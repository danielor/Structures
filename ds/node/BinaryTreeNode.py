
class BinaryTreeNode(object):
    """
    The BinaryTreeNode represents a node in a tree with 2 children
    """
    def __init__(self, data, parent, left, right):
        """
        The main constructor
        :param data The data associated with the node
        :param parent The parent node
        :param left The left node
        :param right The right node
        """
        self.data = data 
        self.parent = parent
        self.left = left 
        self.right = right