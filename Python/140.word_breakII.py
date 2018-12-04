from collections import defaultdict
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = defaultdict(list)
        return self.helper(s, wordDict, memo)
        
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return [""]
        partitions = []
        for word in wordDict:
            if s.startswith(word):
                for partition in self.helper(s[len(word):], wordDict, memo):
                    if partition != "":
                        partitions.append(word + " " + partition)
                    else:
                        partitions.append(word)
        memo[s] = partitions
        return partitions
