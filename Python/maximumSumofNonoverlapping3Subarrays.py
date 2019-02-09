class Solution:
    def maxSumOfThreeSubarrays(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums or len(nums) < 3*k:
            return []
        n = len(nums)
        prefixSum = self.getPrefixSum(nums)
        leftMaxSum = [None] * n
        rightMaxSum = [None] * n
        maxSum = (None, None, None) # (currentSum, start_index, end_index)
        # from left to right
        for end in range(k-1, n):
            start = end - k + 1
            currSum = self.getSumFrom(start, end, prefixSum)
            if maxSum[0] is None or currSum > maxSum[0]:
                maxSum = (currSum, start, end)
            leftMaxSum[end] = maxSum
        # from right to left
        maxSum = (None, None, None)
        for start in reversed(range(0, n - k + 1)):
            end = start + k - 1
            currSum = self.getSumFrom(start, end, prefixSum)
            if maxSum[0] is None or currSum > maxSum[0]:
                maxSum = (currSum, start, end)
            rightMaxSum[start] = maxSum
        # get the middle max sum and return result
        res = []
        maxSum = -float('inf')
        for start in range(k, n - 2*k + 1):
            end = start + k - 1
            midSum = self.getSumFrom(start, end, prefixSum)
            leftMax = leftMaxSum[start-1]
            rightMax = rightMaxSum[end+1]
            if leftMax[0] + midSum + rightMax[0] > maxSum:
                res = [leftMax[1], start, rightMax[1]]
                maxSum = leftMax[0] + midSum + rightMax[0]
        return res
              
    def getSumFrom(self, start:'int', end: 'int', prefixSum: 'List[int]') -> 'int':
        return prefixSum[end + 1] - prefixSum[start]
    
    def getPrefixSum(self, nums:'List[int]') -> 'List[int]':
        n = len(nums)
        sums = [0] * (n+1)
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]
        return sums
