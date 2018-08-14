class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k = len(haystack)-len(needle)
        for i in range(k+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        # if we want to improve the speed of the algorithm, we should learn KMP
        # https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
