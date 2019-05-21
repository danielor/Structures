
class LinkedListNode(object):
    """
    The LinkedListNode represents a node in a linked
    list 
    """
    def __init__(self, data, nextNode = None):
        """
        The constructor for the linked list nodes 
        :param data The data in the node 
        :param next The next pointer 
        """
        self.data = data
        self.nextNode = nextNode  

    def __str__(self):
        """
        A string reprensation of the LinkedListNode 
        """
        return '<LinkListNode ' + str(self.data) + '>'
        