
class Stack(object):
    """
    A representation of a stack in Python
    """
    def __init__(self):
        """
        The constructor of the stack 
        """
        self._data = []

    def __str__(self):
        """
        Return the string representation of Stack 
        """
        s = '['
        nodes = [str(d) for d in self._data]
        s += ", ".join(nodes)
        s += ']'
        return s 

    def isEmpty(self):
        """
        A function that checks if a stack is empty 
        """
        return len(self._data) == 0 

    def push(self, item):
        """
        A function that adds an item to the stack 
        :param item The item to add stack 
        """
        self._data.append(item)

    def pop(self):
        """
        A function that pops the item from the stack 
        """
        return self._data.pop()

    def size(self):
        """
        A function that checks the size of the stack 
        """
        return len(self._data)

    def peek(self):
        """
        A function that returns the top of the stack 
        """
        last_index = self.size() - 1
        return self._data[last_index]
        