class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        p1, p2 = [0] * n, [0] * n
        
        minV, maxV = prices[0], prices[-1]
        for i in range(1, n):
            minV = min(prices[i], minV)
            p1[i] = max(p1[i-1], prices[i] - minV)
            
        for i in range(n-2, -1, -1):
            maxV = max(prices[i], maxV)
            p2[i] = max(p2[i+1], maxV - prices[i])
        
        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res
