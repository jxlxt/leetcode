class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for _ in range(1, rowIndex):
            res = [list(map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1]))]
        return res
