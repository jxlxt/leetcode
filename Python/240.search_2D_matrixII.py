class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        m, n = 0, col - 1
        while row > m and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                m += 1
            else:
                n -= 1
        return False
