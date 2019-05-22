from ds.node.LinkedListNode import LinkedListNode

class LinkedList(object):
    """
    A representation of a linked list in Python
    """
    def __init__(self, head):
        """
        The constructor of the linked list 
        :param head The head of the linked list 
        """
        self.head = head 

    def __str__(self):
        """
        Returns the string representation of node 
        """
        s = '('
        nodes = []
        current = self.head 
        while current:
            nodes.append(str(current.data))
            current = current.nextNode
        s += ", ".join(nodes)
        s += ')'
        return s 

    def find(self, value):
        """
        A function that find the value 
        :param value The value 
        """
        current = self.head 
        while current and current.data != value:
            current = current.nextNode
        return current

    def prepend(self, data):
        """
        A function that inserts the data at the beginning 
        of the data 
        :param data The data to prepend 
        """
        self.head = LinkedListNode(data, self.head)
        
    def append(self, data):
        """
        Insert a new element at the end of the list 
        :param data The data to append
        """
        if not self.head:
            self.head = LinkedListNode(data, self.head)
            return 
        current = self.head 
        while current.nextNode:
            curr = current.nextNode 
        current.nextNode = LinkedListNode(data)

    def remove(self, data):
        """
        A function that removes the node by data 
        :param data The data to append 
        """
        current, prev = self.head, None
        while current and current.data != data:
            prev = current
            current = current.nextNode
        if prev is None:
            self.head = current
        elif current:
            prev.nextNode = current.nextNode
            current.nextNode = None

    def reverse(self):
        """
        A function that reverses a linked list 
        """
        current, prev, nextNode = self.head, None, None
        while current:
            nextNode = current.nextNode 
            current.nextNode = prev 
            prev = current
            current = nextNode
        self.head = prev

