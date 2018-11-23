class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        res, tmp = 0, x
        while tmp:
            res = res * 10 + tmp % 10
            tmp //= 10
        return res == x
