# hint: hashtable save two sum
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        numLen, res, diction = len(nums), set(), {}
        nums.sort()
        for i in range(numLen):
            for j in range(i+1, numLen):
                if nums[i] + nums[j] not in diction:
                    diction[nums[i] + nums[j]] = [(i, j)]
                else:
                    diction[nums[i] + nums[j]].append((i, j))
                    
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                t = target - nums[i] - nums[j]
                if t in diction:
                    for k in diction[t]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
