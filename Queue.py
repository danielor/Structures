
class Queue(object):
    """
    A representation of a queue in Python
    """
    def __init__(self):
        """
        The constructor of the queue 
        """
        self._data = []

    def __str__(self):
        """
        Return the string representation of Queue 
        """
        s = '['
        nodes = [str(d) for d in self._data]
        s += ", ".join(nodes)
        s += ']'
        return s 

    def isEmpty(self):
        """
        A function that checks if a queue is empty 
        """
        return len(self._data) == 0

    def enqueue(self, item):
        """
        A function that enqueue the items
        :param item The item to process 
        """
        self._data.insert(0, item)

    def dequeue(self):
        """
        A function that dequeue the item 
        """
        return self._data.pop()

    def size(self):
        """
        A function that checks the size of the queue 
        """
        return len(self._data)

    def peek(self):
        """
        A function that gets the beggining of the queue 
        """
        last_index = self.size() - 1
        return self._data[last_index]