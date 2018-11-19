class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        # the ways to decode a string = the last digit + the last two digits
        # i from s[0] = 1, s[1], s[2], ..., s[i-1] 
        for i in range(1, len(s)+1):
            # from the last digit
            if (s[i-1] != '0'):
                dp[i] += dp[i-1]
            # from the last two digits, the number should from '10' to '26'
            if (i >= 2 and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'))):
                dp[i] += dp[i-2]                
        return dp[len(s)]
