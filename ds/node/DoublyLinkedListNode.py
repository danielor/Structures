
class DoublyLinkedListNode(object):
    """
    The DoulbyLinkedListNode represents a node in doubly linked list 
    """
    def __init__(self, data, nextNode, prevNode):
        """
        The constructor of the DoublyLinkedListNode
        :param data The data to store in the node 
        :param nextNode A pointer to the next node 
        :param prevNode A pointer to the previous node 
        """
        self.data = data 
        self.nextNode = nextNode 
        self.prevNode = prevNode

    def __str__(self):
        """
        A function that returns the string representation of the doubly linked list 
        """
        return '<DoublyLinkedListNode ' + str(self.data) + '>'
