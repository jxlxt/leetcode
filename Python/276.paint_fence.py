class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0, k, k*k]
        if n <= 2:
            return dp[n]
        if k == 1 and n >= 3:
            return 0
        for i in range(2, n):
            dp.append((k-1) * (dp[-1] + dp[-2]))
        return dp[-1]
            
