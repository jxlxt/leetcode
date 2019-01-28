class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0
        n = len(s)
        mod = 10 ** 9 + 7
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] == '*':
                dp[i] = (dp[i] + dp[i-1] * 9) % mod
                if i >= 2:
                    if s[i-2] == '1':
                        dp[i] = (dp[i] + dp[i-2] * 9) % mod
                    elif s[i-2] == '2':
                        dp[i] = (dp[i] + dp[i-2] * 6) % mod
                    elif s[i-2] == '*':
                        dp[i] = (dp[i] + 15 * dp[i-2]) % mod
            else:
                if s[i-1] >= '1' and s[i-1] <= '9':
                    dp[i] = (dp[i] + dp[i-1]) % mod
                if i >= 2:
                    if s[i-2] == '*':
                        if s[i-1] >= '0' and s[i-1] <= '6':
                            dp[i] = (dp[i] + dp[i-2] * 2) % mod
                        if s[i-1] >= '7' and s[i-1] <= '9':
                            dp[i] = (dp[i] + dp[i-2]) % mod
                    else:
                        twodigits = int(s[i-2:i])
                        if twodigits >= 10 and twodigits <= 26:
                            dp[i] = (dp[i] + dp[i-2]) % mod
        return dp[n]
