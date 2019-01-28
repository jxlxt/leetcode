class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        abbr = False
        self.helper(word, '', abbr, res)
        return res[::-1] # The reverse is only for passing tests
        
    def helper(self, remaining, temp, abbr, res):
        if not remaining:
            res.append(temp)
            return
        self.helper(remaining[1:], temp + remaining[:1], False, res) 
        if not abbr:
            for i in range(1,len(remaining)+1):
                self.helper(remaining[i:], temp + str(len(remaining[:i])), True, res)
