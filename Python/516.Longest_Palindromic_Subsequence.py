class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    # Space complexity: O(n^2)
    def longestPalindromeSubseq(self, s):
#        # write your code here
#        n = len(s)
#        if n == 0:
#            return 0
#        dp = [[0 for _ in range(n)] for _ in range(n)]
#        for i in reversed(range(n)):
#            dp[i][i] = 1 
#            for j in range(i+1, n):
#                if s[i] == s[j]:
#                    dp[i][j] = dp[i+1][j-1] + 2
#                else:
#                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
#        return dp[0][n-1]
        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            pre = dp[j]
            for i in reversed(range(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if j - i >= 2  else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]
