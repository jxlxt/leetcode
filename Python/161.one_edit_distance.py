class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = len(s), len(t)
        if l1 > l2:
            l1, l2, s, t = l2, l1, t, s
        # three situation
        # 1. S length - T length > 1, cannot edit once
        if l2 - l1 > 1 or s == t: return False
        for i in range(l1):
            if s[i] != t[i]:
                # 2. S length - T length = 0, only modify
                if l1 == l2:
                    s = s[:i] + t[i] + s[i+1:]
                # 3. S length - T length = 1, add 
                else:
                    s = s[:i] + t[i] + s[i:]
                break
        return s == t or s == t[:-1]
