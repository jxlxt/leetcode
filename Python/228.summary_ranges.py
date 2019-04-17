class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res, start, end = [], 0, 0
        while end < len(nums) - 1:
            if nums[end] + 1 != nums[end+1]:
                res.append(self.printRange(nums[start], nums[end]))
                start = end + 1
            end += 1
        res.append(self.printRange(nums[start], nums[end]))
        return res
    
    def printRange(self, left, right):
        if left == right:
            return str(left)
        else:
            return str(left) + "->" + str(right)
