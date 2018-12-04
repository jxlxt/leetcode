class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # binary search or golden search
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] < A[mid + 1]:
                left = mid
            elif A[mid - 1] > A[mid]:
                right = mid
            else:
                return mid
    def peakIndexInMountainArray_2(self, A):
        # this algorithm uses golden search
        # although the time complexity is still O(logN) but it use less division
        def gold_1(self, left, right):
            return 1 + int(round(right - left) * 0.382)
        def gold_2(self, left, right):
             return 1 + int(round(right - left) * 0.618)
        left, right = 0, len(A) - 1
        x1, x2 = gold_1(left, right), gold_2(left, right)
        while x1 < x2:
            if A[x1] < A[x2]:
                left = x1
                x1 = x2
                x2 = gold_1(x1, right)
            else:
                right = x2
                x2 = x1
                x1 = gold_2(left, x2)
            return x1
