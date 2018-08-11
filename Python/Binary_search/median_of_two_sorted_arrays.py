class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(nums1), len(nums2)
        if m>n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        i_min, i_max = 0, m
        while i_min <= i_max:
            i = i_min + (i_max - i_min) // 2
            j = (m + n + 1) // 2 - i
            if i < m and B[j-1] > A[i]:
                # mid is too small, must decrease it 
                i_min = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # mid is too big, must decrease it
                i_max = i - 1
            else:
                # mid is perfect
                if i == 0: max_left = B[j-1]
                elif j == 0: max_left = A[i-1]
                else: max_left = max(A[i-1], B[j-1])

                if (m+n)%2 == 1:
                    return max_left

                if i == m: min_right = B[j]
                elif j ==n: min_right = A[i]
                else: min_right = min(A[i], B[j])

                return (max_left+min_right)/2.0
