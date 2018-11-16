class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesis_helper("", res, n, 0, 0)
        return res
    def generateParenthesis_helper(self, curr, res, n, left, right):
        """
        recursion 
        """
        if right == n:
            res.append(curr)
            return
        if left < n:
            self.generateParenthesis_helper(curr+'(', res, n, left+1, right)
        if right < left:
            self.generateParenthesis_helper(curr+')', res, n, left, right+1)
