class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        size = len(word)
        cnt = loc = 0
        for c in abbr:
            if c.isdigit():
                if c == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(c)
            else:
                loc += cnt
                cnt = 0
                if loc >= size or word[loc] != c:
                    return False
                loc += 1
        return cnt + loc == size
