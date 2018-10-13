from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queque = deque(maxlen=size)
        self.size = size
        self.curSum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.curSum += val
        if len(self.queue) == self.size:
            self.curSum -= self.queue.popleft()
        self.queue.append(val)
        return float(self.curSum) / len(self.queue)
