from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # sliding window
        res, p_char_count, s_char_count = [], Counter(p), Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_char_count[s[i]] += 1
            if s_char_count == p_char_count:
                res.append(i - len(p) + 1)
            s_char_count[s[i - len(p) + 1]] -= 1
            if s_char_count[s[i - len(p) + 1]] == 0:
                del s_char_count[s[i - len(p) + 1]]
        return res
