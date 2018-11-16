class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointer
        if height is None or len(height) < 2:
            return 0
        left, right = 0, len(height)-1
        res = temp = 0
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            res = max(res, temp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  
        return res
