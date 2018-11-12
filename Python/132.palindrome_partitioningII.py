class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, f = len(s), []
        p = [[False for x in range(n)] for x in range(n)]
        for i in range(n+1):
            f.append(n-1-i)
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]
