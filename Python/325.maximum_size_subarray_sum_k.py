class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: 'int') -> 'int':
        ans, acc = 0, 0
        # key is the value, value is the index
        hashtable = {0:-1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in hashtable:
                hashtable[acc] = i
            if acc - k in hashtable:
                ans = max(ans, i - hashtable[acc -k])
        return ans
