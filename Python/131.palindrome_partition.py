class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, res, [])
        return res
    
    def dfs(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], res, path+[s[:i]])
    
    def isPalindrome(self, s):
        return s == s[::-1]
