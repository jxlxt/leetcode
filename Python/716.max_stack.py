class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.items[0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.items)

    def popMax(self):
        """
        :rtype: int
        """
        return self.items.pop(self.items.index(max(self.items)))
