class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # dfs solution
        res, candidates = [], sorted(candidates)
        self.dfs(candidates, target, res, 0, [])
        return res
        
    def dfs(self, candidates, target, res, index, path):
        # backtracking 
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            # fine tune
            if candidates[i] > target:
                break
            self.dfs(candidates, target - candidates[i], res, i, path + [candidates[i]]
