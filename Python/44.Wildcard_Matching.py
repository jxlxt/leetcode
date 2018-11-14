class Solution:
    def isMatch(self, source, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # memoery search
        return self.isMatch_helper(source, 0, pattern, 0, {})
        
    def isMatch_helper(self, source, i, pattern, j, memo):
        # determine wheter (i, j) pair in the memo
        if (i, j) in memo:
            return memo[(i, j)]
        # if source is empty, we should make sure that each char in pattern '*'
        if len(source) == i:
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True
        # if pattern is empty, only return false
        if len(pattern) == j:
            return False
        # normal situtaion
        if pattern[j] != '*':
            matched = self.isMatch_char(source[i], pattern[j]) and self.isMatch_helper(source, i+1, pattern, j+1, memo)
        else:
            matched = self.isMatch_helper(source, i+1, pattern, j, memo) or self.isMatch_helper(source, i, pattern, j+1, memo)
        memo[(i, j)] = matched
        return matched
    
    def isMatch_char(self, source, pattern):
        return source == pattern or pattern == '?'
