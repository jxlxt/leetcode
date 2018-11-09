class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[i][j] == 1
                    continue
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]
