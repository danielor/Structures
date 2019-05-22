from ds.node.DoublyLinkedListNode import DoublyLinkedListNode

class DoublyLinkedList(object):
    """
    A representation of a doubly linked list in python
    """
    def __init__(self, head):
        """
        The main constructor
        :param head The head node of the linked list 
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

    def prepend(self, data):
        """
        Insert element on the beginning of the list 
        :param data The data object
        """
        nhead = DoublyLinkedListNode(data, self.head, None)
        if self.head:
            self.head.prevNode = nhead  
        self.head = nhead

    def append(self, data):
        """
        Insert element at the end of the list 
        :param data The data object 
        """
        if not self.head:
            self.head = DoublyLinkedListNode(data, None, None)
            return 
        current = self.head 
        while current.nextNode:
            current = current.nextNode 
        current.nextNode = DoublyLinkedListNode(data, None, current)

    def find(self, key):
        """
        Search for the first element with data 
        :param key The key with data 
        """
        current = self.head 
        while current and current.data != key: 
            current = current.nextNode
        return current

    def remove(self, key):
        """
        A function that searches for a value by key and removes
        it from the linked list 
        """
        current = self.head 
        while current and current.data != key:
            current = current.nextNode
        if not current:
            return 
        if current.prevNode:
            current.prevNode.nextNode = current.nextNode 
        if current.nextNode:
            current.nextNode.prevNode = current.prevNode
        if current == self.head:
            self.head = current.nextNode
        current.prevNode = None 
        current.nextNode = None 

    def reverse(self):
        """
        A function that reverses the linked list 
        """
        current, prev = self.head, None 
        while current:
            prev = current.prevNode 
            current.prevNode = current.nextNode 
            current.nextNode = prev
            current = current.prevNode
        self.head = prev.prevNode