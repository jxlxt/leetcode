class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        hashmap = {}
        myset = set()
        strs = strs.split()
        
        # if length is not match, return False directly
        if len(pattern) != len(strs):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if strs[i] not in myset:
                    hashmap[pattern[i]] = strs[i]
                    myset.add(strs[i])
                else:
                    return False
            if strs[i] != hashmap[pattern[i]]:
                return False
        return True
