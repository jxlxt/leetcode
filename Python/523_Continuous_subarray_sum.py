class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        # time complexity: O(n^2)
        # for i in range(len(nums)):
        #     sums = nums[i]
        #     for j in range(i+1, len(nums)):
        #         sums += nums[j]
        #         if sums == k:
        #             return True
        #         elif k != 0 and sums % k == 0:
        #             return True          
        # return False
        sum_ = 0
        # edge case
        if len(nums) <= 1: return False
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        if k == 0:
            return False
        if k < 0:
            k = -k
        # key is the prefix sum, value is the index
        hashMap = {0:-1}
        for i in range(len(nums)):
            sum_ += nums[i]
            if k != 0:
                sum_ %= k
            if sum_ in hashMap:
                if i - hashMap[sum_] > 1:
                    return True
            else:
                hashMap[sum_] = i
        return False
