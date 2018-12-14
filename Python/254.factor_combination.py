import math
class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], n, 2)
        return res
    
    def helper(self, res, path, num, factor):
        if num <=1:
            if len(path) > 1:
                res.append(path[:])
            return
        
        for i in range(factor, int(math.sqrt(num))+1):
            if num % i == 0:
                path.append(i)
                self.helper(res, path, num // i, i)
                path.pop()
        
        if num >= factor:
            path.append(num)
            self.helper(res, path, 1, num)
            path.pop()
