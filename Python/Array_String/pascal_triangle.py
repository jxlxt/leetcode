class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        Explaination: Any row can be constructed using the offset sum of 
        the previous row.
        """
        res = [[1]]
        for _ in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1]))]
        return res[:numRows]
