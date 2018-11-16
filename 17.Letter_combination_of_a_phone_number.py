class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # BFS solution
        # if not digits: return []
        # ans = [""]
        # d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # for digit in digits:
        #     tmp = []
        #     for s in ans:
        #         for c in d[ord(digit) - ord('0')]:
        #             tmp.append(s+c)
        #     ans = tmp
        # return ans
        # DFS solution
        def dfs(digits, d, l, cur, ans):
            if l == len(digits):
                if l > 0: ans.append("".join(cur))
                return
        
            for c in d[ord(digits[l]) - ord('0')]:
                cur[l] = c
                dfs(digits, d, l + 1, cur, ans)
        
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
        cur = [' ' for _ in range(len(digits))]
        ans = []
        dfs(digits, d, 0, cur, ans)
        return ans
