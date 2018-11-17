class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # corner case
        if not matrix: return matrix
        row, col = len(matrix), len(matrix[0])
        temp = [[matrix[i][j] for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not temp[i][j]:
                    self.setZeroes_helper(i, j, col, row, matrix)
    
    def setZeroes_helper(self, row, col, n, m, matrix):
        for i in range(m):
            matrix[i][col] = 0
        for j in range(n):
            matrix[row][j] = 0
