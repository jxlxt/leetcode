class Solution:  
    def canWin(self, s: str, memo = {}) -> bool:
        if s in memo:
            return memo[s]
        for new_s in (s[:i] + '--' + s[i+2:] for i in range(len(s)-1) if s[i:i+2] == '++'):
            memo[new_s] = self.canWin(new_s)
            if not memo[new_s]:
                memo[s] = True
                break
        else:
            memo[s] = False
        return memo[s]
