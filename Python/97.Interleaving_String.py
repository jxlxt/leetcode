# good explaination: http://www.cnblogs.com/grandyang/p/4298664.html
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, p = len(s1), len(s2), len(s3)
        # corner case
        # if two string s1 and s2 are empty, we just return False
        if m + n != p:
            return False
        # dp initialization
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i== 0 and j == 0:
                    dp[i][j] = True
                # if s1 is emty string, we only need compare s2 and s3
                elif i == 0:
                    dp[i][j] = (s2[:j] == s3[:j])
                # if s2 is empty string, we only need compare s1 and s3
                elif j == 0:
                    dp[i][j] = (s1[:i] == s3[:i])
                # consider both left and top side of possiblity 
                else:
                    dp[i][j] = (s1[i-1] == s3[i-1+j] and dp[i-1][j]) or (s2[j-1] == s3[j-1+i] and dp[i][j-1])
        return dp[-1][-1]
