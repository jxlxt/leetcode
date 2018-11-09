import math
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i - c >= 0 else MAX for c in coins])+1

        if dp[amount] == MAX:
            return -1
        else:
            return dp[amount]


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))
