class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pythonic method
        return s[::-1]
        # classic method
        i, j = 0, len(s)-1
        res = list(s)
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return "".join(res)

